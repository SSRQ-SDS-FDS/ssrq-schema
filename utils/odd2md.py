import re
import xml.etree.ElementTree as ET
from abc import abstractmethod
from pathlib import Path
from typing import (
    Callable,
    Iterator,
    Literal,
    Optional,
    Protocol,
    runtime_checkable,
)

from snakemd import Document  # type: ignore

from utils.main import Schema, load_config, odd_factory
from utils.translater import TRANSLATE, Translations

# default languages used to generate the documentation
LANGS = ["de", "fr"]
# various namespaces used in the ODD
TEI_NS = "http://www.tei-c.org/ns/1.0"
RELAX_NG_NS = "http://relaxng.org/ns/structure/1.0"
XML_NS = "http://www.w3.org/XML/1998/namespace"
NS_MAP = {"tei": TEI_NS, "rng": RELAX_NG_NS, "xml": XML_NS}

RE_PATTERN = re.compile(r"[\s\n]+")


def create_schema_by_entry(entry_point: str) -> Schema | None:
    """Create a schema from the config file.

    Args:
        entry_point (str): The name of the entry point.

    Returns:
        Schema | None: A schema class instance if it exists, None otherwise.
    """
    config = load_config()

    if config is None:
        return None

    schema_config = [
        schema for schema in config.schemas if schema["entry"] == entry_point
    ][0]
    return odd_factory(
        schema_config=schema_config,
        authors=config.authors,
    )


def split_tag_and_ns(tag: str) -> tuple[str, str]:
    """Split a tag into its namespace and its tag name.

    Args:
        tag (str): The tag to split.

    Returns:
        tuple[str, str]: The namespace and the tag name.
    """
    if "}" not in tag:
        return "", tag
    ns, tag_name = tag[1:].split("}")
    return ns, tag_name


ODD_COMP_TYPES = Literal["elementSpec", "classSpec", "dataSpec", "macroSpec"]


@runtime_checkable
class ODDElement(Protocol):
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str
    module: str | None
    classes: list[str] | None

    @abstractmethod
    def to_markdown(
        self, lang: str, lang_translations: dict[str, str], path: Optional[Path] = None
    ) -> Optional[str]:
        ...


class BaseSpec:
    attributes: list[str] | None
    content: dict[str, list[str]] | None
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str
    module: str | None
    classes: list[str] | None = None

    def __init__(self, element: ET.Element) -> None:
        self.odd_element = element
        self.ident = element.attrib["ident"]
        self.module = element.attrib.get("module")

    def find_classes(
        self,
        element: ET.Element,
        components: dict[str, ODDElement] | None = None,
    ) -> list[str] | None:
        """
        Find all classes that the current ODDElement is a member of.
        Works recursively, so it also finds nested classes.

        Args:
            element (ET.Element): The element to search for classes.
            components (dict[str, ODDElement] | None, optional): A dictionary of all components. Defaults to None.

        Returns:
            list[str] | None: A list of all classes that the current ODDElement is a member of.
        """
        classes_found: list[str] | None = None

        classes = element.find("./tei:classes", namespaces=NS_MAP)

        if classes is None or len(classes) == 0:
            # Return early if no classes are found
            return classes_found

        classes_found = []

        for class_elem in element.findall(
            "tei:classes/tei:memberOf", namespaces=NS_MAP
        ):
            class_key = class_elem.attrib["key"]
            class_spec = components.get(class_key) if components else None

            classes_found.append(class_key)

            if class_spec is not None:
                nested_classes = self.find_classes(
                    element=class_spec.odd_element, components=components
                )
                if nested_classes is not None:
                    classes_found.extend(nested_classes)

        return classes_found

    def find_attributes(self) -> list[str] | None:
        att_list = self.odd_element.find("./tei:attList", namespaces=NS_MAP)

        if att_list is None and self.classes is None:
            return None

        assert isinstance(att_list, ET.Element)
        element_attributes = att_list.findall("tei:attDef", namespaces=NS_MAP)

        return (
            [
                attribute.attrib["ident"]
                for attribute in element_attributes
                if attribute.get("mode") != "delete"
            ]
            if element_attributes is not None
            else None
        )

    def find_content_elements(
        self,
        element: ET.Element,
        components: dict[str, ODDElement],
    ) -> list[str] | None:
        """
        Find all possibile content elements, which could occur in the current ODDElement.
        Works recursively, so all macros or datatypes will be expanded.

        Args:
            element (ET.Element): The element to search for content elements.
            components (dict[str, ODDElement]): A dictionary of all components.

        Returns:
            list[str] | None: A list of all possibile content elements."""
        elements_found: list[str] | None = None

        content = element.find("tei:content", namespaces=NS_MAP)

        if content is None or len(content) == 0:
            # Return early if no content is found
            return elements_found

        elements_found = []

        for content_part in content.iter():
            key_or_name = (
                key
                if (key := content_part.attrib.get("key"))
                else content_part.attrib.get("name")
            )
            if key_or_name is not None:
                content_spec = components.get(key_or_name)

                if content_spec is not None:
                    nested_content = self.find_content_elements(
                        element=content_spec.odd_element, components=components
                    )
                    if nested_content is not None:
                        elements_found.extend(nested_content)
                else:
                    elements_found.append(key_or_name)

            if split_tag_and_ns(content_part.tag)[1] == "textNode":
                elements_found.append("textNode")

        return elements_found

    def get_desc(self, lang: str) -> str:
        desc = self.odd_element.find(
            f"./tei:desc[@xml:lang='{lang}']", namespaces=NS_MAP
        )
        if desc is None:
            return ""
        return self._desc_node_to_string(node=desc)

    def _desc_node_to_string(self, node: ET.Element) -> str:
        child_nodes = node.findall("*")

        if len(child_nodes) == 0:
            return RE_PATTERN.sub(" ", node.text) if node.text is not None else ""

        child_nodes_dict: dict[str, ET.Element] = {
            child_node.text.strip(): child_node
            for child_node in node.findall("*")
            if child_node.text is not None
        }

        return RE_PATTERN.sub(
            " ",
            " ".join(
                [
                    self._handle_node_text(
                        child_nodes_dict=child_nodes_dict, text=text.strip()
                    )
                    for text in node.itertext()
                ]
            ),
        )

    def _handle_node_text(
        self,
        child_nodes_dict: dict[str, ET.Element],
        text: str,
        split_tag: Callable[[str], tuple[str, str]] = split_tag_and_ns,
    ) -> str:
        if text in child_nodes_dict.keys():
            child = child_nodes_dict[text]
            child_name = name if (name := split_tag(child.tag)[1]) else child.tag
            match child_name:
                case "gi":
                    return f"[`<{text}/>`]({text}.md)"
                case "att":
                    return f"[@{text})(#{text})"
                case "ref":
                    return f"[{text}]({child.attrib['target']})"
                case _:
                    return text
        return text


class ElementSpec(BaseSpec):
    def __init__(self, element: ET.Element):
        super().__init__(element=element)
        self.odd_type = "elementSpec"

    def to_markdown(
        self, lang: str, lang_translations: dict[str, str], path: Optional[Path] = None
    ) -> Optional[str]:
        doc = Document()
        # Add the name of the element as title
        doc.add_heading(self.ident, level=1)
        self._desc_to_markdown(lang=lang, desc_title=lang_translations["desc"], doc=doc)
        self._create_attribute_desc(
            lang=lang, section_title=lang_translations["attr"], doc=doc
        )

        if path is not None:
            return doc.dump(name=f"{self.ident}.{lang}", dir=path)
        return doc.__str__()

    def _create_attribute_desc(self, lang: str, section_title: str, doc: Document):
        if hasattr(self, "attributes") and self.attributes is None:
            # If the element has no attributes, return
            return None

        self.attributes = self.find_attributes()

        if self.attributes is None:
            return None

        doc.add_heading(section_title, level=2)

    def _desc_to_markdown(self, lang: str, desc_title: str, doc: Document) -> None:
        doc.add_heading(desc_title, level=2)
        doc.add_paragraph(self.get_desc(lang=lang))


class ClassSpec(BaseSpec):
    def __init__(self, element: ET.Element):
        super().__init__(element=element)
        self.odd_type = "classSpec"

    def to_markdown(
        self, lang: str, lang_translations: dict[str, str], path: Optional[Path] = None
    ) -> Optional[str]:
        pass


class DataSpec:
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str
    classes: list[str] | None
    module: str | None

    def __init__(self, element: ET.Element):
        self.odd_element = element
        self.odd_type = "dataSpec"
        self.ident = element.attrib["ident"]
        self.module = element.attrib.get("module")
        self.classes = None

    def to_markdown(
        self, lang: str, lang_translations: dict[str, str], path: Optional[Path] = None
    ) -> Optional[str]:
        pass


class MacroSpec(BaseSpec):
    def __init__(self, element: ET.Element):
        super().__init__(element=element)
        self.odd_type = "macroSpec"

    def to_markdown(
        self, lang: str, lang_translations: dict[str, str], path: Optional[Path] = None
    ) -> Optional[str]:
        pass


class ODDReader:
    odd: ET.Element
    elements: dict[str, ElementSpec]
    components: dict[str, ODDElement]
    translations: Translations

    def __init__(self, odd: str, translations: Translations = TRANSLATE):
        self.odd = ET.fromstring(odd)
        self.elements = {spec.ident: spec for spec in self._get_element_specs()}
        self.components = {
            component.ident: component
            for component in self._get_component_specs()
            if isinstance(component, ODDElement)
        }
        self.translations = translations

    def _get_component_specs(self) -> Iterator[ClassSpec | DataSpec | MacroSpec]:
        from itertools import chain

        class_specs = [
            ClassSpec(element=class_spec)
            for class_spec in self.odd.findall(".//tei:classSpec", namespaces=NS_MAP)
        ]
        data_specs = [
            DataSpec(element=data_spec)
            for data_spec in self.odd.findall(".//tei:dataSpec", namespaces=NS_MAP)
        ]
        macro_specs = [
            MacroSpec(element=macro_spec)
            for macro_spec in self.odd.findall(".//tei:macroSpec", namespaces=NS_MAP)
        ]
        return chain(class_specs, data_specs, macro_specs)

    def _get_element_specs(self) -> list[ElementSpec]:
        el_specs = self.odd.findall(".//tei:elementSpec", namespaces=NS_MAP)
        return [ElementSpec(element=el_spec) for el_spec in el_specs]


class ODD2Md:
    """A class which helps to streamline the process of converting ODD files to Markdown."""

    schema: ODDReader
    languages: list[str]
    el_spec_name: str = "elementSpec"
    out_dir: Path

    def __init__(
        self, schema: Schema | str, languages: list[str], target_dir: str
    ) -> None:
        """Initialize the class.

        Args:
            schema (Schema): The schema class instance.
            languages (list[str]): The languages to convert.
        """
        self.out_dir = Path(target_dir)
        self.languages = languages
        self.schema = ODDReader(
            odd=schema.compiled_odd if isinstance(schema, Schema) else schema
        )

    def create_md_doc_per_lang(self) -> None:
        """Create a markdown documentation per element per language.

        Returns:
            None: Nothing."""

        for _, element in self.schema.elements.items():
            for lang in self.languages:
                element.to_markdown(
                    lang=lang,
                    lang_translations=getattr(self.schema.translations, lang),
                    path=self.out_dir,
                )

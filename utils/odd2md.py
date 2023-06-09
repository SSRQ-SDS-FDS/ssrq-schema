import re
import xml.etree.ElementTree as ET
from abc import abstractmethod
from pathlib import Path
from typing import Literal, Optional, Protocol, runtime_checkable

from snakemd import Document  # type: ignore

from utils.main import Schema, load_config, odd_factory

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


ODD_COMP_TYPES = Literal["elementSpec", "classSpec", "dataSpec", "macroSpec"]


@runtime_checkable
class ODDElement(Protocol):
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str

    @property
    def classes(self) -> list[str] | None:
        ...

    @abstractmethod
    def to_markdown(self, lang: str, path: Optional[Path] = None) -> Optional[str]:
        ...


class BaseSpec:
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str

    @property
    def classes(self) -> list[str] | None:
        classes = self.odd_element.find("./tei:class", namespaces=NS_MAP)
        if classes is None:
            return None
        member_of = classes.findall(".//tei:memberOf", namespaces=NS_MAP)
        return [member.attrib["key"] for member in member_of]

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
        self, child_nodes_dict: dict[str, ET.Element], text: str
    ) -> str:
        if text in child_nodes_dict.keys():
            child = child_nodes_dict[text]
            child_name = name if (name := child.tag.split("}")[1]) else child.tag
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
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str

    def __init__(self, element: ET.Element):
        self.odd_element = element
        self.odd_type = "elementSpec"
        self.ident = element.attrib["ident"]

    def to_markdown(self, lang: str, path: Optional[Path] = None) -> Optional[str]:
        doc = Document()
        doc.add_heading(self.ident, level=1)
        doc.add_paragraph(self.get_desc(lang=lang))

        if path is not None:
            return doc.dump(name=f"{self.ident}.{lang}", dir=path)
        return doc.__str__()


class DataSpec:
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str

    def __init__(self, element: ET.Element):
        self.odd_element = element
        self.odd_type = "dataSpec"
        self.ident = element.attrib["ident"]

    @property
    def classes(self) -> list[str] | None:
        return None

    def to_markdown(self, lang: str, path: Optional[Path] = None) -> Optional[str]:
        pass


class ODDReader:
    odd: ET.Element
    elements: list[str]
    components: dict[str, ODDElement]

    def __init__(self, odd: str):
        self.odd = ET.fromstring(odd)
        elements = self._get_element_specs()
        self.elements = [spec.ident for spec in elements]
        self.components = {spec.ident: spec for spec in self._get_element_specs()}

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

        for element in self.schema.elements:
            component = self.schema.components[element]
            for lang in self.languages:
                component.to_markdown(lang=lang, path=self.out_dir)

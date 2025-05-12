import xml.etree.ElementTree as ET
from typing import Literal, cast

from snakemd import Document  # type: ignore

from utils.commons.logger import LOGGER
from utils.docs.helpers.sort import sort_with_uca
from utils.docs.helpers.utils import split_tag_and_ns, translate_datatype
from utils.docs.specs.namespaces import NS_MAP
from utils.docs.specs.oddelement import ODDElement

UsageStatus = Literal["opt", "rec", "req"]


class AttributeSpec:
    attr_element: ET.Element
    content: list[ET.Element] | None
    classes: list[ET.Element] | None
    ident: str
    usage_status: UsageStatus

    def __init__(
        self,
        element: ET.Element,
        element_classes: list[ET.Element] | None,
    ) -> None:
        self.attr_element = element
        self.ident = element.attrib["ident"]
        self.classes = element_classes
        self._add_description()
        self._get_usage_status()

    def add_content(self, components: dict[str, ODDElement]) -> None:
        self.content = self._resolve_content(
            element=self.attr_element, components=components
        )

    def content_values_to_markdown(
        self, doc: Document, lang: str, translations: dict[str, str]
    ) -> None:
        """
        Transforms the content values of the attribute to markdown and adds them to the
        document. If the attribute has no content values, nothing is added to the
        document.

        Args:
            doc (Document): The document to add the content values to.
        """
        if self.content is None:
            return

        output: list[str] = []
        for content_part in self.content:
            _, tag_name = split_tag_and_ns(content_part.tag)
            match tag_name:
                case "data":
                    name_translation = (
                        translate_datatype(name, translations=translations)
                        if (name := content_part.get("type"))
                        else ""
                    )
                    restriction = (
                        f" – {translations['restriction']}: {translations[name] + ' ' if (name := param.get('name')) else ''}`{param.text}`"
                        if (param := content_part.find("rng:param", namespaces=NS_MAP))
                        is not None
                        else ""
                    )
                    output.append(f"{name_translation}{restriction}")

                case "dataRef":
                    name_translation = (
                        translate_datatype(name, translations=translations)
                        if (name := content_part.get("name"))
                        else ""
                    )
                    restriction = (
                        f" – {translations['restriction']}: {translations['pattern']} `{r}`"
                        if (r := content_part.get("restriction"))
                        else ""
                    )
                    output.append(f"{name_translation}{restriction}")

                case "ref":
                    LOGGER.warning(
                        f"Ignored unresolved ref {content_part.get('name')} in attribute {self.ident}"
                    )

                case "valItem":
                    val_item_rendered = content_part.attrib["ident"]

                    desc = content_part.find(
                        f"tei:desc[@xml:lang = '{lang}']", namespaces=NS_MAP
                    )

                    if desc is not None:
                        val_item_rendered += f"  - *{self._render_description(desc)}*"

                    output.append(val_item_rendered)

                case _:
                    raise ValueError(
                        f"Can't convert to markdown. Unexpected tag name: {tag_name}"
                    )

        doc.add_paragraph(f"*{translations['values']}*")
        doc.add_unordered_list(sort_with_uca(output))

    def _add_description(self) -> None:
        """Add the description of the attribute to the attribute element if it does not
        exist.
        """

        desc = self.attr_element.find("./tei:desc", namespaces=NS_MAP)

        if desc is not None:
            return

        if self.classes is None:
            return

        class_descriptions: list[ET.Element] = []

        for element_class in self.classes:
            attribute = element_class.findall(
                f".//tei:attDef[@ident = '{self.ident}']",
                namespaces=NS_MAP,
            )
            if len(attribute) > 0:
                for a in attribute:
                    class_descriptions.extend(
                        a.findall("./tei:desc", namespaces=NS_MAP)
                    )

        if len(class_descriptions) > 0:
            for index, description in enumerate(class_descriptions):
                self.attr_element.insert(index, description)

    def _get_definition(self, context: ET.Element) -> ET.Element | None:
        definitions = []

        for child in context:
            if split_tag_and_ns(child.tag)[1] not in [
                "constraintSpec",
                "desc",
                "gloss",
                "exemplum",
            ]:
                definitions.append(child)

        if len(definitions) == 0:
            if self.classes is None:
                return None

            class_containing_attribute = [
                class_with_attr
                for c in self.classes
                if (
                    class_with_attr := c.find(
                        f".//tei:attDef[@ident = '{self.ident}']", namespaces=NS_MAP
                    )
                )
                is not None
            ]

            if len(class_containing_attribute) == 0:
                return None

            for class_containing_attr in class_containing_attribute:
                d = self._get_definition(context=class_containing_attr)
                if d is not None:
                    definitions.append(d)

        return definitions[0]

    def _get_usage_status(self) -> None:
        usage_attr = self.attr_element.get("usage")

        if usage_attr is not None:
            self.usage_status = cast(UsageStatus, usage_attr)
            return

        if self.classes is not None:
            for spec in self.classes:
                if (
                    att_def := spec.find(
                        f".//tei:attDef[@ident = '{self.ident}'][@usage]",
                        namespaces=NS_MAP,
                    )
                ) is not None:
                    self.usage_status = cast(UsageStatus, att_def.get("usage"))
                    return

        self.usage_status = "opt"

    def _render_description(self, context: ET.Element) -> str:
        return f"{context.text or ''}{
            ''.join(self._render_description_child(child) for child in context)
        }"

    def _render_description_child(self, context: ET.Element) -> str:
        _, tag = split_tag_and_ns(context.tag)
        match tag:
            case "hi":
                return f"<sup>{context.text}</sup>{context.tail or ''}"
            case _:
                LOGGER.warning(f"Unsupported child tag in description »{tag}»")
                return ""

    def _resolve_content(
        self, element: ET.Element, components: dict[str, ODDElement]
    ) -> list[ET.Element] | None:
        """
        Args:
            element (ET.Element): The element to search for content elements.
            components (dict[str, ODDElement]): A dictionary of all components.

        Returns:
            list[ET.Element] | None: A list of all content values of the attribute / spec.

        """
        values_found: list[ET.Element] | None = None

        data = self._get_definition(context=element)

        if data is None:
            return values_found

        values_found = []

        for content_part in data.iter():
            _, tag_name = split_tag_and_ns(content_part.tag)

            key_or_name: str | None = None

            match tag_name:
                case "data":
                    key_or_name = content_part.get("type")
                case "dataRef":
                    key_or_name = (
                        key
                        if (key := content_part.get("key"))
                        else content_part.get("name")
                    )
                case "ref":
                    key_or_name = content_part.get("name")
                case _:
                    key_or_name = None

            if key_or_name is not None:
                content_spec = components.get(key_or_name)

                if content_spec is not None:
                    nested_content = self._resolve_content(
                        element=content_spec.odd_element, components=components
                    )
                    if nested_content is not None:
                        values_found.extend(nested_content)
                else:
                    values_found.append(content_part)

            if split_tag_and_ns(content_part.tag)[1] == "valList":
                val_items = content_part.findall("./tei:valItem", namespaces=NS_MAP)
                values_found.extend(val_items)
                break

        return values_found

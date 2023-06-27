import xml.etree.ElementTree as ET

from utils.specs.abstract import ODDElement
from utils.specs.config import NS_MAP
from utils.specs.utils import split_tag_and_ns


class AttributeSpec:
    attr_element: ET.Element
    content: list[ET.Element] | None
    classes: list[ET.Element] | None
    ident: str

    def __init__(
        self,
        element: ET.Element,
        element_classes: list[ET.Element] | None,
    ) -> None:
        self.attr_element = element
        self.ident = element.attrib["ident"]
        self.classes = element_classes
        self._add_description()

    def add_content(self, components: dict[str, ODDElement]) -> None:
        self.content = self._resolve_content(
            element=self.attr_element, components=components
        )

    def _add_description(self) -> None:
        """Add the description of the attribute to the attribute element if it does not
        exist.
        """

        desc = self.attr_element.find("./tei:desc", namespaces=NS_MAP)

        if desc is not None:
            return None

        if self.classes is None:
            return None

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
                "exemplum",
            ]:
                definitions.append(child)

        if len(definitions) == 0:
            return None

        return definitions[0]

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
            key_or_name = (
                key
                if (key := content_part.attrib.get("key"))
                else content_part.attrib.get("name")
            )
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

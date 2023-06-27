import xml.etree.ElementTree as ET

from utils.specs.abstract import ODDElement
from utils.specs.config import NS_MAP
from utils.specs.utils import split_tag_and_ns


class AttributeSpec:
    attr_element: ET.Element
    content: list[str | ET.Element]
    classes: list[ET.Element] | None
    ident: str

    def __init__(
        self, element: ET.Element, element_classes: list[ET.Element] | None
    ) -> None:
        self.attr_element = element
        self.ident = element.attrib["ident"]
        self.classes = element_classes
        self._add_description()

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

    def _add_content(self) -> None:
        ...

    def _get_definition(self) -> ET.Element | None:
        definitions = []

        for child in self.attr_element:
            if split_tag_and_ns(child.tag)[1] not in [
                "constraintSpec",
                "desc",
                "exemplum",
            ]:
                definitions.append(child)

        if len(definitions) == 0:
            return None

        return definitions[0]

    def resolve_content(
        self, components: dict[str, ODDElement]
    ) -> list[str | ET.Element] | None:
        ...

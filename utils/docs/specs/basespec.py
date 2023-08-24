import re
import xml.etree.ElementTree as ET

from utils.docs.specs.abstract import ODD_COMP_TYPES, ODDElement
from utils.docs.specs.attributespec import AttributeSpec
from utils.docs.specs.namespaces import NS_MAP
from utils.docs.specs.utils import split_tag_and_ns

RE_WHITESPACE_PATTERN = re.compile(r"[\s\n]+")


class BaseSpec:
    attributes: list[AttributeSpec] | None
    content: list[str | ET.Element] | None
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str
    module: str | None
    classes: list[str] | None = None

    def __init__(self, element: ET.Element) -> None:
        self.odd_element = element
        self.ident = element.attrib["ident"]
        self.module = element.attrib.get("module")

    def _compare_element_with_class_attributes(
        self,
        element_attributes: list[ET.Element] | None,
        element_classes: list[ET.Element] | None,
        class_attributes: list[ET.Element] | None,
    ) -> list[AttributeSpec] | None:
        """A helper function to compare the attributes of an element with the attributes
        of its classes.

        Args:
            element_attributes (list[ET.Element] | None): The attributes of the element.
            class_attributes (list[ET.Element] | None): The attributes of the classes.

        Returns:
            list[AttributeSpec] | None: The attributes of the element including those
                not deleted and defined in the class."""

        def get_attributes_not_deleted(
            attributes: list[ET.Element],
        ) -> list[ET.Element]:
            return [
                attribute
                for attribute in attributes
                if attribute.get("mode") != "delete"
            ]

        if element_attributes is None and class_attributes is None:
            return None

        if class_attributes is None and element_attributes is not None:
            return [
                AttributeSpec(attr, element_classes=element_classes)
                for attr in get_attributes_not_deleted(element_attributes)
            ]

        if element_attributes is None and class_attributes is not None:
            return [
                AttributeSpec(attr, element_classes=element_classes)
                for attr in get_attributes_not_deleted(class_attributes)
            ]

        assert element_attributes is not None
        assert class_attributes is not None

        ident_element_attributes_deleted = [
            attribute.get("ident")
            for attribute in element_attributes
            if attribute.get("mode") == "delete"
        ]
        attributes_not_deleted = get_attributes_not_deleted(element_attributes)
        ident_attributes_not_deleted = [
            attribute.get("ident") for attribute in attributes_not_deleted
        ]
        class_attributes = get_attributes_not_deleted(class_attributes)

        for class_attr in class_attributes:
            ident = class_attr.get("ident")
            assert ident is not None
            if (
                ident not in ident_element_attributes_deleted
                and ident not in ident_attributes_not_deleted
            ):
                attributes_not_deleted.append(class_attr)

        return [
            AttributeSpec(element=attribute, element_classes=element_classes)
            for attribute in attributes_not_deleted
        ]

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

    def find_examples(self) -> list[ET.Element] | None:
        examples = self.odd_element.findall("tei:exemplum", namespaces=NS_MAP)

        if examples is None or len(examples) == 0:
            return None

        return examples

    def find_attributes(
        self, components: dict[str, ODDElement]
    ) -> list[AttributeSpec] | None:
        att_list = self.odd_element.find("./tei:attList", namespaces=NS_MAP)

        if self.classes is None:
            self.classes = self.find_classes(
                element=self.odd_element, components=components
            )

        if att_list is None and self.classes is None:
            return None

        assert isinstance(att_list, ET.Element)
        class_attributes: list[ET.Element] | None = None
        element_classes: list[ET.Element] | None = None

        if self.classes is not None:
            class_attributes = []
            element_classes = []
            for c in self.classes:
                component = components.get(c)
                if component is not None:
                    attributes = self._get_attributes_from_class(component.odd_element)
                    if attributes is not None:
                        class_attributes.extend(attributes)
                    element_classes.append(component.odd_element)

        if class_attributes is not None and len(class_attributes) == 0:
            class_attributes = None

        element_attributes = (
            el_attr
            if len(el_attr := att_list.findall("./tei:attDef", namespaces=NS_MAP)) > 0
            else None
        )

        if element_attributes is None and class_attributes is None:
            return None

        attribute_specs = self._compare_element_with_class_attributes(
            element_attributes=element_attributes,
            class_attributes=class_attributes,
            element_classes=element_classes,
        )

        if attribute_specs is None:
            return None

        return (
            specs
            if (
                specs := [
                    spec
                    for spec in attribute_specs
                    if spec.attr_element.get("mode") != "delete"
                ]
            )
            else None
        )

    def find_content_elements(
        self,
        element: ET.Element,
        components: dict[str, ODDElement],
    ) -> list[str | ET.Element] | None:
        """
        Find all possibile content elements, which could occur in the current ODDElement.
        Works recursively, so all macros or datatypes will be expanded.

        Args:
            element (ET.Element): The element to search for content elements.
            components (dict[str, ODDElement]): A dictionary of all components.

        Returns:
            list[str] | None: A list of all possibile content elements."""
        elements_found: list[str | ET.Element] | None = None

        content = element.find("tei:content", namespaces=NS_MAP)

        if content is None or len(content) == 0:
            # Return early if no content is found
            return elements_found

        if content.find("tei:empty", namespaces=NS_MAP) is not None:
            # Also return early if the content is empty
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

            if split_tag_and_ns(content_part.tag)[1] == "valList":
                elements_found.append(content_part)

            if split_tag_and_ns(content_part.tag)[1] == "textNode":
                elements_found.append("textNode")

        return elements_found

    def example_to_string(
        self, example: ET.Element, lang: str
    ) -> tuple[str | None, str]:
        """
        Convert an tei:exemplum to a string.

        Args:
            example (ET.Element): The example to convert.
            lang (str): The language of the output.

        Returns:
            tuple[str | None, str]: A tuple containing the title and the code of the example.

        Raises:
            ValueError: If the example does not contain any example code.
        """

        example_title = example.find("./tei:p", namespaces=NS_MAP)
        example_code = example.find("./teiEx:egXML", namespaces=NS_MAP)

        if example_code is None:
            raise ValueError("Example does not contain any code.")

        ET.indent(example_code, space="    ", level=0)

        return (
            self._desc_node_to_string(desc=example_title)
            if example_title is not None
            else None,
            ET.tostring(example_code, encoding="unicode", method="xml").replace(
                "ns0:", ""
            ),
        )

    def _get_attributes_from_class(
        self, odd_class: ET.Element
    ) -> list[ET.Element] | None:
        att_list = odd_class.find("./tei:attList", namespaces=NS_MAP)

        if att_list is None:
            return None

        assert isinstance(att_list, ET.Element)
        class_attributes = att_list.findall("./tei:attDef", namespaces=NS_MAP)

        return class_attributes if len(class_attributes) > 0 else None

    def get_desc(self, element: ET.Element, lang: str, upper: bool = True) -> str:
        desc = element.find(f"./tei:desc[@xml:lang='{lang}']", namespaces=NS_MAP)

        if desc is None:
            return ""
        description_rendered = self._desc_node_to_string(desc=desc)

        return (
            self._upper_desc_start(desc=description_rendered)
            if upper
            else description_rendered
        )

    def get_remarks(
        self, element: ET.Element, lang: str, upper: bool = True
    ) -> str | list[str] | None:
        remark = element.find(f"./tei:remarks[@xml:lang='{lang}']", namespaces=NS_MAP)

        remark_content: str | list[str]

        if remark is None:
            return None

        remark_paragraphs = remark.findall("./tei:p", namespaces=NS_MAP)

        if len(remark_paragraphs) == 0:
            remark_content = (
                self._upper_desc_start(desc=self._desc_node_to_string(desc=remark))
                if upper
                else self._desc_node_to_string(desc=remark)
            )
        else:
            remark_content = [
                self._upper_desc_start(desc=self._desc_node_to_string(desc=p))
                if upper
                else self._desc_node_to_string(desc=p)
                for p in remark_paragraphs
            ]

        return remark_content

    def _upper_desc_start(self, desc: str) -> str:
        return desc[0].upper() + desc[1:]

    def _desc_node_to_string(self, desc: ET.Element):
        """
        This method converts a desc like node to a string.

        Args:
            desc (ET.Element): The desc like node.

        Returns:
            str: The string representation of the desc like node.

        ToDo:
            * Fix the bug that leading whitespace, which has a meaning, is removed.
        """
        output = ""
        if desc.text is not None:
            output += RE_WHITESPACE_PATTERN.sub(" ", desc.text)
        if len(desc) > 0:
            for child in desc:
                tag_name = split_tag_and_ns(child.tag)[1]
                tail_text = (
                    RE_WHITESPACE_PATTERN.sub(" ", child.tail)
                    if child.tail is not None
                    else ""
                )
                child_text = (
                    RE_WHITESPACE_PATTERN.sub(" ", child.text)
                    if child.text is not None
                    else ""
                )
                match tag_name:
                    case "gi":
                        output += f"[`<{child_text}/>`]({child_text}.md){tail_text if tail_text.startswith('-') else ' ' + tail_text}".strip()
                    case "att":
                        output += f"[@{child_text}](#{child_text}) {tail_text}".strip()
                    case "ref":
                        output += f"[{child_text}]({child.attrib['target']}) {tail_text}".strip()
                    case "list":
                        output += "\n\n" + "\n".join(
                            [
                                "- " + self._desc_node_to_string(child)
                                for child in child
                                if isinstance(child, ET.Element)
                            ]
                        )
                    case "tag":
                        output += f"`<{child_text}/>` {tail_text}"
                    case "val":
                        output += f"`{child_text}` {tail_text}"
                    case _:
                        output += (child_text + tail_text).strip()
        return re.sub((r"\s+([\.,:;])"), r"\1", output)

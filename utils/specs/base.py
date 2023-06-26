import re
import xml.etree.ElementTree as ET
from typing import Callable

from utils.specs.abstract import ODD_COMP_TYPES, ODDElement
from utils.specs.attribute import AttributeSpec
from utils.specs.config import NS_MAP
from utils.specs.utils import split_tag_and_ns

RE_PATTERN = re.compile(r"[\s\n]+")


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
                AttributeSpec(attr, class_attributes if class_attributes else [])
                for attr in get_attributes_not_deleted(element_attributes)
            ]

        if element_attributes is None and class_attributes is not None:
            return [
                AttributeSpec(attr, class_attributes)
                for attr in get_attributes_not_deleted(class_attributes)
            ]

        assert element_attributes is not None
        assert class_attributes is not None

        class_attributes = get_attributes_not_deleted(class_attributes)

        return [
            AttributeSpec(attribute, class_attributes)
            for attribute in class_attributes
            if not any(
                [
                    el_attribute.get("ident") == attribute.get("ident")
                    and el_attribute.get("mode") == "delete"
                    for el_attribute in element_attributes
                ]
            )
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
        class_attributes = (
            [
                self._get_attributes_from_class(component.odd_element)
                for c in self.classes
                if (component := components.get(c)) is not None
            ]
            if self.classes is not None
            else None
        )

        if class_attributes is not None:
            # flatten the list of lists using a list comprehension and filter out None values
            class_attributes = [
                attribute  # type: ignore
                for attributes in class_attributes
                if attributes is not None
                for attribute in attributes
            ]

            if len(class_attributes) == 0:
                class_attributes = None

        element_attributes = (
            el_attr
            if len((el_attr := att_list.findall("./tei:attDef", namespaces=NS_MAP))) > 0
            else None
        )

        if element_attributes is None and class_attributes is None:
            return None

        return self._compare_element_with_class_attributes(
            element_attributes=element_attributes, class_attributes=class_attributes  # type: ignore
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
                val_items = content_part.findall("./tei:valItem", namespaces=NS_MAP)
                elements_found.extend(val_items)

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
            self._desc_node_to_string(node=example_title)
            if example_title is not None
            else None,
            re.sub(
                r'<egXML (xmlns:ns\d=".*")+>',
                "<egXML>",
                ET.tostring(example_code, encoding="unicode", method="xml").replace(
                    "ns0:", ""
                ),
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

    def get_desc(self, element: ET.Element, lang: str) -> str:
        desc = element.find(f"./tei:desc[@xml:lang='{lang}']", namespaces=NS_MAP)

        if desc is None:
            return ""
        return self._desc_node_to_string(node=desc)

    def _desc_node_to_string(
        self, node: ET.Element, start_with_upper: bool = True
    ) -> str:
        def upper_desc_start(desc: str, upper: bool) -> str:
            if not upper:
                return desc
            return desc[0].upper() + desc[1:]

        child_nodes = node.findall("*")

        if len(child_nodes) == 0:
            return (
                upper_desc_start(
                    desc=RE_PATTERN.sub(" ", node.text), upper=start_with_upper
                )
                if node.text is not None
                else ""
            )

        child_nodes_dict: dict[str, ET.Element] = {
            child_node.text.strip(): child_node
            for child_node in node.findall("*")
            if child_node.text is not None
        }

        return upper_desc_start(
            RE_PATTERN.sub(
                " ",
                " ".join(
                    [
                        self._handle_node_text(
                            child_nodes_dict=child_nodes_dict, text=text.strip()
                        )
                        for text in node.itertext()
                    ]
                ),
            ),
            upper=start_with_upper,
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
                    return f"[@{text}](#{text})"
                case "ref":
                    return f"[{text}]({child.attrib['target']})"
                case _:
                    return text
        return text

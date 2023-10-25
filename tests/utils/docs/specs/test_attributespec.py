import xml.etree.ElementTree as ET

from utils.docs.specs.attributespec import AttributeSpec
from utils.docs.specs.namespaces import NS_MAP

ET.register_namespace("tei", NS_MAP["tei"])


def test_attribute_without_usage_and_class_has_usage_opt():
    element = ET.Element("attDef", attrib={"ident": "foo"})
    attribute = AttributeSpec(element, None)

    attribute._get_usage_status()

    assert attribute.usage_status == "opt"


def test_attribute_with_usage_status():
    element = ET.Element("attDef", attrib={"ident": "foo", "usage": "rec"})
    attribute = AttributeSpec(element, None)

    attribute._get_usage_status()

    assert attribute.usage_status == "rec"


def test_attribute_without_usage_status_with_class():
    element = ET.Element("attDef", attrib={"ident": "foo"})
    example_class = ET.Element(
        "classSpec",
        attrib={
            "ident": "bar",
        },
    )
    class_attribute_definition = ET.Element(
        ET.QName(NS_MAP["tei"], "attDef"),
        attrib={"ident": "foo", "usage": "rec"},  # type: ignore
    )
    example_class.append(class_attribute_definition)
    attribute = AttributeSpec(element, element_classes=[example_class])

    attribute._get_usage_status()

    assert attribute.usage_status == "rec"

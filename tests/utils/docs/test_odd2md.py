import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from utils.docs.odd2md import (
    LANGS,
    ODD2Md,
    ODDReader,
)
from utils.docs.specs.abstract import ODDElement
from utils.docs.specs.attribute import AttributeSpec
from utils.docs.specs.element import ElementSpec
from utils.docs.specs.ns import NS_MAP
from utils.docs.specs.utils import split_tag_and_ns

from .conftest import EL_FINDER, check_result_with_xpath


def test_creation_of_md_files_per_el(example_odd: str, tmp_path: Path):
    elements = check_result_with_xpath(
        xml=example_odd, xpath="count(//tei:elementSpec)", expected_result=None
    )
    if elements is not None:
        elements = int(elements.__str__()) * len(LANGS)
        odd2md = ODD2Md(schema=example_odd, languages=LANGS, target_dir=tmp_path)
        odd2md.create_md_doc_per_lang()
        assert len(list(tmp_path.glob("*.md"))) == elements


def test_find_classes_non_recursive(example_elementSpec: EL_FINDER):
    example_el_spec = example_elementSpec("p")
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)
    assert isinstance(el_spec, ODDElement)
    assert el_spec.odd_element == example_el_spec
    assert el_spec.ident == "p"
    assert el_spec.odd_type == "elementSpec"
    el_spec.classes = el_spec.find_classes(element=el_spec.odd_element)
    assert el_spec.classes is not None
    assert len(el_spec.classes) == int(
        check_result_with_xpath(
            ET.tostring(example_el_spec, encoding="unicode"),
            xpath="count(.//tei:classes/tei:memberOf)",
            expected_result=None,
        ).__str__()
    )


def test_find_classes_recursive(
    example_elementSpec: EL_FINDER, example_odd: str, tmp_path: Path
):
    odd_reader = ODDReader(odd=example_odd)
    example_el_spec = example_elementSpec("p")
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)
    assert isinstance(el_spec, ODDElement)
    assert el_spec.odd_element == example_el_spec
    assert el_spec.ident == "p"
    assert el_spec.odd_type == "elementSpec"
    el_spec.classes = el_spec.find_classes(
        element=el_spec.odd_element, components=odd_reader.components
    )
    assert el_spec.classes is not None
    assert len(el_spec.classes) == 5


@pytest.mark.parametrize(
    "element_name, has_content, xpath",
    [
        (
            "hi",
            True,
            "count(//tei:macroSpec[starts-with(@ident, 'ssrq.content')]//tei:elementRef|//tei:macroSpec[starts-with(@ident, 'ssrq.content')]//tei:textNode)",
        ),
        ("addSpan", False, None),
        ("delSpan", False, None),
        ("damage", True, "4"),
    ],
)
def test_find_el_content(
    example_elementSpec: EL_FINDER,
    example_odd: str,
    element_name: str,
    has_content: bool,
    xpath: str | None,
):
    """
    Test if the content of an element is found correctly.

    Args:
        example_elementSpec (EL_FINDER): Fixture to find an elementSpec in the example ODD.
        example_odd (str): Fixture to find the example ODD.
        element_name (str): Name of the element to find.
        has_content (bool): Whether the element has content or not.
        xpath (str | None): XPath expression to find the content of the element.

    Returns:
        None"""

    odd_reader = ODDReader(odd=example_odd)
    example_el_spec = example_elementSpec(element_name)

    assert example_el_spec is not None

    el_spec = ElementSpec(element=example_el_spec)

    assert el_spec.odd_type == "elementSpec"

    el_spec.content = el_spec.find_content_elements(
        element=el_spec.odd_element, components=odd_reader.components  # type: ignore
    )

    if has_content:
        assert el_spec.content is not None
    else:
        assert el_spec.content is None

    if has_content:
        assert isinstance(el_spec.content, list)

        if xpath is not None:
            default_content_elements = check_result_with_xpath(
                xml=example_odd,
                xpath=xpath,
                expected_result=None,
            )
            assert len(el_spec.content) == int(default_content_elements.__str__())


@pytest.mark.parametrize(
    "element_name, has_attributes, attributes",
    [
        (
            "bibl",
            False,
            None,
        ),
        ("hi", True, ["rend", "hand"]),
        ("term", True, ["ref"]),
        ("material", True, ["type"]),
    ],
)
def test_find_el_attributes(
    example_elementSpec: EL_FINDER,
    example_odd: str,
    element_name: str,
    has_attributes: bool,
    attributes: list[str] | None,
):
    odd_reader = ODDReader(odd=example_odd)
    example_el_spec = example_elementSpec(element_name)
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)
    assert el_spec.odd_type == "elementSpec"
    el_spec.attributes = el_spec.find_attributes(
        components=odd_reader.components  # type: ignore
    )
    assert bool(el_spec.attributes) is has_attributes
    if has_attributes:
        assert attributes is not None
        assert isinstance(el_spec.attributes, list)
        assert len(el_spec.attributes) == len(attributes)
        for attribute in el_spec.attributes:
            assert isinstance(attribute, AttributeSpec)
            assert attribute.ident in attributes


@pytest.mark.parametrize(
    "element_name, attribute, classes",
    [
        (
            "date",
            "period",
            ["att.datable"],
        ),
    ],
)
def test_attribute_classes(
    example_elementSpec: EL_FINDER,
    example_odd: str,
    element_name: str,
    attribute: str,
    classes: list[str],
):
    odd_reader = ODDReader(odd=example_odd)
    example_el_spec = example_elementSpec(element_name)
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)
    assert el_spec.odd_type == "elementSpec"
    el_spec.attributes = el_spec.find_attributes(
        components=odd_reader.components  # type: ignore
    )
    assert el_spec.attributes is not None
    attribute_spec = [attr for attr in el_spec.attributes if attr.ident == attribute]
    assert len(attribute_spec) == 1
    attribute_spec = attribute_spec[0]
    assert isinstance(attribute_spec, AttributeSpec)
    assert attribute_spec.classes is not None
    attribute_classes = [class_.get("ident") for class_ in attribute_spec.classes]
    for c in classes:
        assert c in attribute_classes


@pytest.mark.parametrize(
    "element_name, attribute, lang_and_text",
    [
        (
            "date",
            "dur-iso",
            [("de", "Erfassung Zeitspanne nach"), ("fr", "Saisie Période")],
        ),
    ],
)
def test_resolved_attribute_descriptions(
    example_elementSpec: EL_FINDER,
    example_odd: str,
    element_name: str,
    attribute: str,
    lang_and_text: list[tuple[str, str]],
):
    odd_reader = ODDReader(odd=example_odd)
    example_el_spec = example_elementSpec(element_name)
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)
    assert el_spec.odd_type == "elementSpec"
    el_spec.attributes = el_spec.find_attributes(
        components=odd_reader.components  # type: ignore
    )
    assert el_spec.attributes is not None
    attribute_spec = [attr for attr in el_spec.attributes if attr.ident == attribute]
    assert len(attribute_spec) == 1
    attribute_spec = attribute_spec[0]
    assert isinstance(attribute_spec, AttributeSpec)
    for lang, text in lang_and_text:
        lang_desc = attribute_spec.attr_element.find(
            f"tei:desc[@xml:lang = '{lang}']", namespaces=NS_MAP
        )
        assert lang_desc is not None
        assert lang_desc.text is not None
        assert text in lang_desc.text


def test_spec_desc_to_md(example_elementSpec: EL_FINDER):
    example_el_spec = example_elementSpec("p")
    assert example_elementSpec is not None
    el_spec = ElementSpec(element=example_el_spec)
    desc = el_spec.get_desc(element=el_spec.odd_element, lang="de")
    assert isinstance(desc, str)
    assert "\n" not in desc
    desc_childs = el_spec.odd_element.findall(
        "tei:desc[@xml:lang = 'de']/*", namespaces=NS_MAP
    )
    if desc_childs is not None:
        for child in desc_childs:
            match split_tag_and_ns(child.tag)[1]:
                case "gi":
                    assert f"[`<{child.text}/>`]({child.text}.md)" in desc
                case "att":
                    assert f"[@{child.text}](#{child.text})" in desc
                case "ref":
                    assert f"[{child.text}]({child.attrib['target']})" in desc
                case _:
                    assert child.text in desc


def test_odd_reader_components_setup(example_odd: str, tmp_path: Path):
    odd_reader = ODDReader(odd=example_odd)
    components = check_result_with_xpath(
        xml=example_odd,
        xpath="count(//tei:classSpec|//tei:macroSpec|//tei:dataSpec)",
        expected_result=None,
    )
    assert components is not None
    assert int(components.__str__()) == len(odd_reader.components)
    for _, component in odd_reader.components.items():
        assert isinstance(component, ODDElement)


def test_find_examples(
    example_odd: str,
    example_elementSpec: EL_FINDER,
):
    example_el_spec = example_elementSpec("measureGrp")
    el_spec = ElementSpec(element=example_el_spec)  # type: ignore
    assert example_el_spec is not None
    examples = el_spec.find_examples()
    assert examples is not None
    examples_check = check_result_with_xpath(
        xml=example_odd,
        xpath="count(//tei:elementSpec[@ident = 'measureGrp']//tei:exemplum)",
        expected_result=None,
    )
    assert len(examples) == int(examples_check.__str__())


def test_example_to_string(
    example_odd: str,
    example_elementSpec: EL_FINDER,
):
    example_el_spec = example_elementSpec("measureGrp")
    el_spec = ElementSpec(element=example_el_spec)  # type: ignore
    assert example_el_spec is not None
    examples = el_spec.find_examples()
    assert examples is not None
    for example in examples:
        example_string = el_spec.example_to_string(example=example, lang="de")
        assert example_string is not None
        assert isinstance(example_string, tuple)
        assert len(example_string) == 2
        assert example_string[0] is not None
        assert isinstance(example_string[1], str)
        assert "measure" in example_string[1]
        assert "type" in example_string[1]


@pytest.mark.parametrize(
    "element_name, attribute_name, content_len",
    [
        (
            "gap",
            "reason",
            3,
        ),
        (
            "add",
            "rend",
            2,
        ),
        ("delSpan", "spanTo", 1),
    ],
)
def test_attribute_content(
    example_elementSpec: EL_FINDER,
    example_odd: str,
    element_name: str,
    attribute_name: str,
    content_len: int,
):
    odd_reader = ODDReader(odd=example_odd)
    example_el_spec = example_elementSpec(element_name)
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)
    assert el_spec.odd_type == "elementSpec"
    el_spec.attributes = el_spec.find_attributes(
        components=odd_reader.components  # type: ignore
    )
    assert el_spec.attributes is not None
    attribute_spec = [
        attr for attr in el_spec.attributes if attr.ident == attribute_name
    ]
    assert len(attribute_spec) == 1
    attribute_spec = attribute_spec[0]
    assert isinstance(attribute_spec, AttributeSpec)
    attribute_spec.add_content(odd_reader.components)
    assert hasattr(attribute_spec, "content")
    assert attribute_spec.content is not None
    assert len(attribute_spec.content) == content_len


@pytest.mark.parametrize(
    "element_name, has_remarks, lang, text",
    [
        (
            "note",
            True,
            "de",
            [
                "Ein [`<note/>`](note.md)-Element folgt unmittelbar auf das Bezugswort im Editionstext",
                "Handelt es sich um eine Anmerkung",
            ],
        ),
    ],
)
def test_remarks_to_markdown(
    example_elementSpec: EL_FINDER,
    example_odd: str,
    element_name: str,
    has_remarks: bool,
    lang: str,
    text: list[str] | str,
):
    example_el_spec = example_elementSpec(element_name)
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)

    remarks = el_spec.get_remarks(element=el_spec.odd_element, lang=lang)

    if not has_remarks:
        assert remarks is None
    else:
        assert remarks is not None

        if isinstance(remarks, list):
            assert len(remarks) == len(text)
            for index, t in enumerate(text):
                assert t in remarks[index]
        else:
            assert remarks in text

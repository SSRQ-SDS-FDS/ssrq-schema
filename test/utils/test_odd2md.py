import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from utils.odd2md import (
    LANGS,
    NS_MAP,
    AttributeSpec,
    ElementSpec,
    ODD2Md,
    ODDElement,
    ODDReader,
    split_tag_and_ns,
)

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


def test_find_el_content(
    example_elementSpec: EL_FINDER, example_odd: str, tmp_path: Path
):
    odd_reader = ODDReader(odd=example_odd)
    example_el_spec = example_elementSpec("hi")
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)
    assert el_spec.odd_type == "elementSpec"
    el_spec.content = el_spec.find_content_elements(
        element=el_spec.odd_element, components=odd_reader.components  # type: ignore
    )
    assert el_spec.content is not None
    assert isinstance(el_spec.content, list)
    default_content_elements = check_result_with_xpath(
        xml=example_odd,
        xpath="count(//tei:macroSpec[starts-with(@ident, 'ssrq.content')]//tei:elementRef|//tei:macroSpec[starts-with(@ident, 'ssrq.content')]//tei:textNode)",
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
            descriptions = attribute.attr_element.findall("tei:desc", namespaces=NS_MAP)
            assert len(descriptions) > 1
            assert len(descriptions) <= 4


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

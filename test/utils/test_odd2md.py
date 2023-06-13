import xml.etree.ElementTree as ET
from pathlib import Path

from utils.odd2md import LANGS, NS_MAP, ElementSpec, ODD2Md, split_tag_and_ns

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


def test_class_el_spec_init(example_elementSpec: EL_FINDER):
    example_el_spec = example_elementSpec("p")
    assert example_el_spec is not None
    el_spec = ElementSpec(element=example_el_spec)
    assert el_spec.odd_element == example_el_spec
    assert el_spec.ident == "p"
    assert el_spec.odd_type == "elementSpec"
    assert len(el_spec.classes) == int(
        check_result_with_xpath(
            ET.tostring(example_el_spec, encoding="unicode"),
            xpath="count(.//tei:classes/tei:memberOf)",
            expected_result=None,
        ).__str__()
    )


def test_class_el_spec_desc_to_md(example_elementSpec: EL_FINDER):
    example_el_spec = example_elementSpec("p")
    assert example_elementSpec is not None
    el_spec = ElementSpec(element=example_el_spec)
    desc = el_spec.get_desc(lang="de")
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

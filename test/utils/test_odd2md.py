from pathlib import Path

import pytest

from utils.odd2md import ODD2Md, XsltParam, apply_xsl

from .conftest import check_result_with_xpath


@pytest.mark.parametrize(
    "params, xpath, result",
    [
        (
            [
                XsltParam(
                    name="modes",
                    type="xs:string",
                    value=["add-att-descriptions"],
                ),
            ],
            "count(//tei:attDef[not(tei:desc)][not(@mode = 'delete')]) = 0",
            True,
        ),
        (
            [
                XsltParam(name="modes", type="xs:string", value=["invalid-mode"]),
            ],
            "count(//tei:attDef[not(./tei:desc)][not(./@mode = 'delete')]) = 0",
            False,
        ),
        (
            [
                XsltParam(
                    name="modes", type="xs:string", value=["resolve-keys-and-names"]
                ),
            ],
            "count(//tei:attDef[tei:datatype[tei:dataRef[@key]]]) = 0",
            True,
        ),
    ],
)
def test_modes_resolve_ref_xsl(
    example_odd: str, params: list[XsltParam], xpath: str, result: bool
):
    xsl_name = "resolve-internal-references.xsl"
    transform = apply_xsl(xml=example_odd, xsl_name=xsl_name, params=params)
    check_result_with_xpath(xml=transform, xpath=xpath, expected_result=result)


def test_creation_of_md_files_per_el(example_odd: str, tmp_path: Path):
    elements = check_result_with_xpath(
        xml=example_odd, xpath="count(//tei:elementSpec)", expected_result=None
    )
    if elements is not None:
        elements = int(elements.__str__())
        odd2md = ODD2Md(schema=example_odd, languages=["de"], target_dir=tmp_path)
        odd2md.create_md_doc_per_lang()
        assert len(list(tmp_path.glob("*.md"))) == elements

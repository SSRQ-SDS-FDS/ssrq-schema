import pytest

from .conftest import XsltParam, apply_xsl, check_result_with_xpath


@pytest.mark.parametrize(
    "params, xpath, result",
    [
        (
            [
                XsltParam(
                    name="modes",
                    type="xs:string",
                    value=["add-att-descirptions"],
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
    ],
)
def test_modes_resolve_ref_xsl(
    example_odd: str, params: list[XsltParam], xpath: str, result: bool
):
    xsl_name = "resolve-internal-references.xsl"
    transform = apply_xsl(xml=example_odd, xsl_name=xsl_name, params=params)
    check_result_with_xpath(xml=transform, xpath=xpath, result=result)

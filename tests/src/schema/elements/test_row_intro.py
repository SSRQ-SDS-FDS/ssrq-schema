import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-row-with-cell",
            "<row><cell>foo</cell></row>",
            True,
        ),
        (
            "valid-row-with-multiple-cells",
            "<row><cell>foo</cell><cell>bar</cell></row>",
            True,
        ),
        (
            "invalid-row-with-measureGrp",
            """
            <row>
                <measureGrp>
                     <cell><measure type="currency" quantity="2" unit="fl">11</measure></cell>
                    <cell><measure type="currency" unit="xr" quantity="15">15</measure></cell>
                </measureGrp>
            </row>
            """,
            False,
        ),
        (
            "invalid-row-with-wrong-content",
            "<row><p>foo</p></row>",
            False,
        ),
    ],
)
def test_row(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("row", name, markup, result, False)

import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sic",
            "<sic>bar</sic>",
            True,
        ),
        (
            "valid-sic-with-mixed-content",
            """
            <sic>
                <add place='above'>foo</add>
                <del>foo</del>
                <lb/>bar
                <note>foo</note>
                <pb/>
                <subst>
                    <add place='above'>foo</add>
                    <del>foo</del>
                </subst>
                <persName>foo</persName>
            </sic>
            """,
            True,
        ),
        (
            "invalid-sic-with-wrong-content",
            "<sic><p>foo</p></sic>",
            False,
        ),
    ],
)
def test_sic(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("sic", name, markup, result, False)

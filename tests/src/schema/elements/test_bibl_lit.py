import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-bibl",
            "<bibl>foo</bibl>",
            True,
        ),
        (
            "invalid-bibl-with-attr",
            "<bibl type='lit'>foo</bibl>",
            False,
        ),
        (
            "invalid-bibl-with-default-content",
            "<bibl><p>foo</p></bibl>",
            False,
        ),
    ],
)
def test_bibl(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("bibl", name, markup, result, False)

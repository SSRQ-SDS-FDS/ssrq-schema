import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-listBibl",
            "<listBibl><head type='literature'>bar</head><bibl>foo</bibl></listBibl>",
            True,
        ),
        (
            "invalid-listBibl-without-head",
            "<listBibl><bibl>foo</bibl></listBibl>",
            False,
        ),
        (
            "invalid-listBibl-without-bibl",
            "<listBibl><head type='literature'>bar</head></listBibl>",
            False,
        ),
    ],
)
def test_listBibl(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("listBibl", name, markup, result, False)

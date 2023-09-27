import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-listBibl",
            "<listBibl type='literature'><bibl>foo</bibl></listBibl>",
            True,
        ),
        (
            "invalid-listBibl-without-type",
            "<listBibl><bibl>foo</bibl></listBibl>",
            False,
        ),
        (
            "invalid-listBibl-without-bibl",
            "<listBibl type='literature'/>",
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

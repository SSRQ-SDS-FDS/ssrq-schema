import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-additional",
            "<additional><listBibl><head type='literature'>bar</head><bibl>foo</bibl></listBibl></additional>",
            True,
        ),
        (
            "invalid-additional-without-listBibl",
            "<additional/>",
            False,
        ),
    ],
)
def test_additional(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("additional", name, markup, result, False)

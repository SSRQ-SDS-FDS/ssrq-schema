import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "simple-valid-bibl",
            "<bibl>foo</bibl>",
            True,
        ),
        (
            "invalid-simple-bibl-with-attr",
            "<bibl type='lit'>foo</bibl>",
            False,
        ),
        (
            "valid-bibl-with-ref",
            "<bibl><ref target='http://zotero.org/groups/5048222/items/M8D9EG5B'/>, S. 93</bibl>",
            True,
        ),
    ],
)
def test_bibl(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("bibl", name, markup, result, False)

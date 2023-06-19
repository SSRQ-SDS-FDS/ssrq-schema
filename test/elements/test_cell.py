from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-cell", "<cell>foo</cell>", True),
        (
            "valid-cell",
            "<cell role='label'>foo</cell>",
            True,
        ),
        (
            "valid-cell",
            "<cell>foo <anchor xml:id='del1'/></cell>",
            True,
        ),
        (
            "cell-with-invalid-attr",
            "<cell xml:id='bar'>foo</cell>",
            False,
        ),
        (
            "invalid-cell",
            "<cell role='bar'>foo</cell>",
            False,
        ),
        (
            "invalid-cell",
            '<cell foo="bar"><teiHeader/></cell>',
            False,
        ),
    ],
)
def test_cell(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("cell", name, markup, result, False)

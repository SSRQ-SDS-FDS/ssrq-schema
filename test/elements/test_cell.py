from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-cell", "<cell xmlns='http://www.tei-c.org/ns/1.0'>foo</cell>", True),
        (
            "valid-cell",
            "<cell xmlns='http://www.tei-c.org/ns/1.0' role='label'>foo</cell>",
            True,
        ),
        (
            "valid-cell",
            "<cell xmlns='http://www.tei-c.org/ns/1.0'>foo <anchor xml:id='bar'/></cell>",
            True,
        ),
        (
            "invalid-cell",
            "<cell xmlns='http://www.tei-c.org/ns/1.0' role='bar'>foo</cell>",
            False,
        ),
        (
            "invalid-cell",
            '<cell xmlns="http://www.tei-c.org/ns/1.0" foo="bar"><teiHeader/></cell>',
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

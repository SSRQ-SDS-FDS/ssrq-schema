import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pubPlace",
            "<pubPlace>foo</pubPlace>",
            True,
        ),
        (
            "valid-pubPlace-with-cert",
            "<pubPlace cert='low'>foo-low</pubPlace>",
            True,
        ),
        (
            "invalid-pubPlace",
            "<pubPlace><p/></pubPlace>",
            False,
        ),
        (
            "invalid-text-with-attributes",
            "<pubPlace type='foobar'>foo</pubPlace>",
            False,
        ),
        (
            "valid-pubPlace-with-invalid-cert",
            "<pubPlace cert='medium'>foo-medium</pubPlace>",
            False,
        ),
    ],
)
def test_pubPlace(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("pubPlace", name, markup, result, False)

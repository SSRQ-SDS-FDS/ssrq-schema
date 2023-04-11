import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pubPlace",
            "<pubPlace xmlns='http://www.tei-c.org/ns/1.0'>foo</pubPlace>",
            True,
        ),
        (
            "invalid-pubPlace",
            "<pubPlace xmlns='http://www.tei-c.org/ns/1.0'><p/></pubPlace>",
            False,
        ),
        (
            "invalid-text-with-attributes",
            "<pubPlace type='foobar' xmlns='http://www.tei-c.org/ns/1.0'>foo</pubPlace>",
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


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-pubPlace",
            "<pubPlace xmlns='http://www.tei-c.org/ns/1.0'>foo</pubPlace>",
            True,
        ),
        (
            "invalid-pubPlace",
            "<pubPlace xmlns='http://www.tei-c.org/ns/1.0'/>",
            False,
        ),
    ],
)
def test_pubPlace_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints defined for tei:pubPlace."""
    writer.write(name, markup)
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result

import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-measureGrp",
            "<measureGrp><lb/><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure></measureGrp>",
            True,
        ),
        (
            "invalid-measureGrp-without-content",
            "<measureGrp/>",
            False,
        ),
        (
            "invalid-measureGrp-with-attribute",
            "<measureGrp type='foo'><lb/></measureGrp>",
            False,
        ),
        (
            "invalid-measureGrp-with-one-measure",
            "<measureGrp><lb/><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure></measureGrp>",
            False,
        ),
    ],
)
def test_measureGrp(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("measureGrp", name, markup, result, False)

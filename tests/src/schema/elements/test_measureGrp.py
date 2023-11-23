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
            "valid-measureGrp",
            "<measureGrp><lb/><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure> und <measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure></measureGrp>",
            True,
        ),
        (
            "valid-measureGrp-with-cells",
            """<measureGrp>
                    <cell><measure type="currency" quantity="2" unit="fl">11</measure></cell>
                    <cell><measure type="currency" unit="xr" quantity="15">15</measure></cell>
                </measureGrp>""",
            True,
        ),
        (
            "invalid-measureGrp-with-one-cell",
            """<measureGrp>
                    <cell><measure type="currency" quantity="2" unit="fl">11</measure></cell>
                </measureGrp>""",
            False,
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


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-measureGrp-with-cells-but-without-measure",
            """<measureGrp>
                    <cell>foo</cell>
                    <cell>foo</cell>
                </measureGrp>""",
            False,
        ),
    ],
)
def test_measureGrp_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result

import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-measureGrp",
            """
            <measureGrp>
                <measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure> 
                <measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure>
            </measureGrp>
            """,
            True,
        ),
        (
            "invalid-measureGrp-with-one-measure",
            """
            <measureGrp>
                <measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure>
            </measureGrp>
            """,
            False,
        ),
        (
            "valid-measureGrp-with-text-content",
            """
            <measureGrp>
                <measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure> 
                und
                <measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure>
            </measureGrp>
            """,
            True,
        ),
        (
            "valid-measureGrp-with-lb",
            """
            <measureGrp>
                <lb/><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure> 
                <lb/><measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure>
            </measureGrp>
            """,
            True,
        ),
        (
            "valid-measureGrp-with-app",
            """
            <measureGrp>
                <measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure>
                <app>
                    <rdg wit="id-ssrq-b28b8ec0-a86a-4c80-8af3-4eb7264a3957">
                        <measure type="currency" unit="ß" quantity="10">10 </measure>
                    </rdg>
                </app>
                <measure quantity='5' unit='ß' type='currency'>fuͤnf schilling pfenig</measure>
            </measureGrp>
            """,
            True,
        ),
        (
            "valid-measureGrp-with-cells",
            """
            <measureGrp>
                <cell><measure type="currency" quantity="2" unit="fl">11</measure></cell>
                <cell><measure type="currency" unit="xr" quantity="15">15</measure></cell>
            </measureGrp>
            """,
            True,
        ),
        (
            "invalid-measureGrp-with-one-cell",
            """
            <measureGrp>
                <cell><measure type="currency" quantity="2" unit="fl">11</measure></cell>
            </measureGrp>
            """,
            False,
        ),
    ],
)
def test_measure_grp(
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
            """
            <measureGrp>
                <cell>foo</cell>
                <cell>foo</cell>
            </measureGrp>
            """,
            False,
        ),
    ],
)
def test_measure_grp_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

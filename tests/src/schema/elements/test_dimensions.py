import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-dimensions-with-two-children",
            """
            <dimensions type='leaves'>
                <height unit='cm' quantity='16.0'/>
                <width unit='cm' quantity='23.0'/>
            </dimensions>
            """,
            True,
        ),
        (
            "valid-dimensions-with-width-only",
            """
            <dimensions type='leaves'>
                <width unit='cm' quantity='23.0'/>
            </dimensions>
            """,
            True,
        ),
        (
            "invalid-dimensions-with-height-only",
            """
            <dimensions type='leaves'>
                <height unit='cm' quantity='23.0'/>
            </dimensions>
            """,
            False,
        ),
    ],
)
def test_dimensions_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("dimensions", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-dimensions-plica-with-height",
            """
            <dimensions type='plica'>
                <height unit='cm' quantity='16.0'/>
                <width unit='cm' quantity='23.0'/>
            </dimensions>
            """,
            False,
        ),
    ],
)
def test_dimensions_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

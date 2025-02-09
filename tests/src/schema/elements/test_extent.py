import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-extent-with-one-dimensions",
            """
            <extent>
                <dimensions type='leaves'>
                    <height unit='cm' quantity='16.0'/>
                    <width unit='cm' quantity='23.0'/>
                </dimensions>
            </extent>""",
            True,
        ),
        (
            "valid-extent-with-two-dimensions",
            """
            <extent>
                <dimensions type='leaves'>
                    <height unit='cm' quantity='16.0'/>
                    <width unit='cm' quantity='23.0'/>
                </dimensions>
                <dimensions type='plica'>
                    <width unit='cm' quantity='4.0'/>
                </dimensions>
            </extent>""",
            True,
        ),
    ],
)
def test_extent_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("extent", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-extent-with-doubled-dimensions-type",
            """
            <extent>
                <dimensions type='leaves'>
                    <height unit='cm' quantity='16.0'/>
                    <width unit='cm' quantity='23.0'/>
                </dimensions>
                <dimensions type='leaves'>
                    <width unit='cm' quantity='4.0'/>
                </dimensions>
            </extent>""",
            False,
        ),
    ],
)
def test_extent_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

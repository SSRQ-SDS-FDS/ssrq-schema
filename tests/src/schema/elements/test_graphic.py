import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-graphic",
            "<graphic type='map' mimeType='image/svg' url='foo.svg'/>",
            True,
        ),
        (
            "invalid-graphic-without-type",
            "<graphic mimeType='image/svg' url='foo.svg'/>",
            False,
        ),
        (
            "invalid-graphic-without-mimeType",
            "<graphic type='map' url='foo.svg'/>",
            False,
        ),
        (
            "invalid-graphic-without-url",
            "<graphic type='map' mimeType='image/svg'/>",
            False,
        ),
        (
            "invalid-graphic-with-content",
            "<graphic type='map' mimeType='image/svg' url='foo.png'>bar</graphic>",
            False,
        ),
    ],
)
def test_graphic(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("graphic", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-graphic-with-correct-url",
            "<graphic type='map' mimeType='image/svg' url='foo.svg'/>",
            True,
        ),
        (
            "invalid-graphic-with-incorrect-url",
            "<graphic type='map' mimeType='image/svg' url='a/foo.svg'/>",
            False,
        ),
    ],
)
def test_graphic_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

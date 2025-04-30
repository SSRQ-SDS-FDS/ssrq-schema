import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-graphic",
            "<graphic url='foo.svg'/>",
            True,
        ),
        (
            "invalid-graphic-with-mimeType",
            "<graphic mimeType='image/svg' url='foo.svg'/>",
            False,
        ),
        (
            "invalid-graphic-with-type",
            "<graphic type='map' url='foo.svg'/>",
            False,
        ),
        (
            "invalid-graphic-without-url",
            "<graphic/>",
            False,
        ),
        (
            "invalid-graphic-with-content",
            "<graphic url='foo.png'>bar</graphic>",
            False,
        ),
    ],
)
def test_graphic(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("graphic", name, markup, result, False)


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
    intro_constraints: str,
    writer: SimpleTEIWriter,
    name: str,
    markup: str,
    result: bool,
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=intro_constraints
    )
    assert reports[0].report.is_valid() is result

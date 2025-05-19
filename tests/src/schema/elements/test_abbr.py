import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-abbr",
            "<abbr>bar</abbr>",
            True,
        ),
        (
            "valid-abbr-with-hi",
            "<abbr><hi rend='sup'>foo</hi>bar</abbr>",
            True,
        ),
        (
            "valid-abbr-with-lb",
            "<abbr>foo<lb/>bar</abbr>",
            True,
        ),
        (
            "valid-abbr-with-sic",
            "<abbr><sic>foobar</sic></abbr>",
            True,
        ),
        (
            "valid-abbr-with-unclear",
            "<abbr><unclear>foobar</unclear></abbr>",
            True,
        ),
        (
            "valid-abbr-with-subst",
            "<abbr><subst><del>bar></del><add place='above'>baz</add></subst></abbr>",
            True,
        ),
    ],
)
def test_abbr(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("abbr", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-abbr-without-points",
            "<abbr>etc</abbr>",
            True,
        ),
        (
            "invalid-abbr-with-points",
            "<abbr>etc.</abbr>",
            False,
        ),
    ],
)
def test_abbr_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )

    if (
        reports[0].report.is_valid() is not result
        and reports[0].report.failed_asserts is not None
    ):
        print("\nSchematron error message: " + reports[0].report.failed_asserts[0].text)

    assert reports[0].report.is_valid() is result

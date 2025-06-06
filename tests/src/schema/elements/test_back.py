import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-back",
            "<back><div><p>foo</p></div></back>",
            True,
        ),
        (
            "valid-back-with-multiple-divs",
            "<back><div><p>foo</p></div><div><p>foo</p></div></back>",
            True,
        ),
        (
            "invalid-back-with-p-only",
            "<back><p>foo</p></back>",
            False,
        ),
        (
            "invalid-back-with-attribute",
            "<back xml:id='bar123'><div><p>foo</p></div></back>",
            False,
        ),
    ],
)
def test_back(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("back", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-back-without-note",
            """
            <back>
                <div>
                    <p>foo</p>
                </div>
            </back>
            """,
            True,
        ),
        (
            "invalid-back-with-note",
            """
            <back>
                <div>
                    <p>foo<note>bar</note></p>
                </div>
            </back>
            """,
            False,
        ),
    ],
)
def test_back_constraints(
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

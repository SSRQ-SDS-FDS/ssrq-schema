import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-persName-with-text-content", "<persName>foo</persName>", True),
        (
            "valid-persName-with-content-default",
            "<persName><del>foo</del> bar</persName>",
            True,
        ),
        (
            "valid-persName-with-ref",
            "<persName ref='per123456'>bar</persName>",
            True,
        ),
        (
            "valid-persName-with-role",
            "<persName ref='per000001' role='witness'>bar</persName>",
            True,
        ),
    ],
)
def test_pers_name(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("persName", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-persName-inside-editor",
            """
            <editor><persName>foo</persName></editor>
            """,
            True,
        ),
        (
            "invalid-persName-inside-editor-ref",
            """
            <editor><persName ref="per123456">foo</persName></editor>
            """,
            False,
        ),
        (
            "invalid-persName-inside-editor-role",
            """
            <editor><persName role="witness">foo</persName></editor>
            """,
            False,
        ),
    ],
)
def test_pers_name_constraints(
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

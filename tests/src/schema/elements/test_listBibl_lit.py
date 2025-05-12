import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-listBibl",
            """
            <listBibl>
                <head>Archiv 1</head>
                <bibl>foo</bibl>
            </listBibl>
            """,
            True,
        ),
        (
            "valid-listBibl-with-multiple-bibls",
            """
            <listBibl>
                <head>Archiv 1</head>
                <bibl>foo</bibl>
                <bibl>foo</bibl>
            </listBibl>
            """,
            True,
        ),
        (
            "invalid-listBibl-with-just-one-listBibl",
            """
            <listBibl>
                <head>Archiv</head>
                <listBibl>
                    <head>Urkunden</head>
                    <bibl>foo</bibl>
                </listBibl>
            </listBibl>
            """,
            False,
        ),
        (
            "valid-listBibl-with-listBibls",
            """
            <listBibl>
                <head>Archiv</head>
                <listBibl>
                    <head>Urkunden</head>
                    <bibl>foo</bibl>
                </listBibl>
                <listBibl>
                    <head>Drucke</head>
                    <bibl>foo</bibl>
                </listBibl>
            </listBibl>
            """,
            True,
        ),
        (
            "invalid-listBibl-without-head",
            "<listBibl><bibl>foo</bibl></listBibl>",
            False,
        ),
        (
            "invalid-listBibl-without-bibl",
            "<listBibl><head>Archiv 1</head></listBibl>",
            False,
        ),
        (
            "invalid-listBibl-with-attribute",
            """
            <listBibl type="foo">
                <head>Archiv 1</head>
                <bibl>foo</bibl>
            </listBibl>
            """,
            False,
        ),
    ],
)
def test_list_bibl(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("listBibl", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-listBibl",
            """
            <listBibl>
                <head>Archiv 1</head>
                <bibl>foo</bibl>
            </listBibl>
            """,
            True,
        ),
        (
            "valid-listBibl-with-listBibl",
            """
            <listBibl>
                <head>Archiv 1</head>
                <listBibl>
                    <head>Urkunden</head>
                    <bibl>foo</bibl>
                </listBibl>
            </listBibl>
            """,
            True,
        ),
        (
            "invalid-listBibl-with-two-many-nesting-levels",
            """
            <listBibl>
                <head>Archiv 1</head>
                <listBibl>
                    <head>Urkunden</head>
                    <listBibl>
                        <head>12.-14. Jh.</head>
                        <bibl>foo</bibl>
                    </listBibl>
                    <listBibl>
                        <head>13.-15. Jh.</head>
                        <bibl>foo</bibl>
                    </listBibl>
                </listBibl>
            </listBibl>
            """,
            False,
        ),
    ],
)
def test_listBibl_constraints(
    lit_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=lit_constraints
    )

    if (
        reports[0].report.is_valid() is not result
        and reports[0].report.failed_asserts is not None
    ):
        print("\nSchematron error message: " + reports[0].report.failed_asserts[0].text)

    assert reports[0].report.is_valid() is result

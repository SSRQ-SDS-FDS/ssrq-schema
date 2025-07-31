import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msContents",
            "<msContents><msItem><textLang xml:lang='de'/></msItem></msContents>",
            True,
        ),
        (
            "valid-msContents-with-summary",
            """
            <msContents>
                <summary xml:lang='de'><p>Foo</p></summary>
                <msItem><textLang xml:lang="de"/></msItem>
            </msContents>
            """,
            True,
        ),
        (
            "invalid-msContents-with-wrong-order",
            """
            <msContents>
                <msItem><textLang xml:lang="de"/></msItem>
                <summary xml:lang='de'><p>Foo</p></summary>
            </msContents>
            """,
            False,
        ),
        (
            "valid-msContents-with-multiple-summaries",
            """
            <msContents>
                <summary xml:lang='de'><p>Foo</p></summary>
                <summary xml:lang='fr'><p>Foo</p></summary>
                <msItem><textLang xml:lang="de"/></msItem>
            </msContents>
            """,
            True,
        ),
        (
            "invalid-msContents-without-msItem",
            """
            <msContents>
                <summary xml:lang='de'><p>Foo</p></summary>
            </msContents>
            """,
            False,
        ),
    ],
)
def test_element(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("msContents", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msContents-with-two-summaries",
            """
            <msContents>
                <summary xml:lang='de'><p>Foo</p></summary>
                <summary xml:lang='fr'><p>Foo</p></summary>
            </msContents>
            """,
            True,
        ),
        (
            "invalid-msContents-with-two-summaries-having-the-same-language",
            """
            <msContents>
                <summary xml:lang='de'><p>Foo</p></summary>
                <summary xml:lang='de'><p>Foo</p></summary>
            </msContents>
            """,
            False,
        ),
    ],
)
def test_msContents_constraints(
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

import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-body-with-div",
            "<body><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-ab",
            "<body><ab type='dorsal' place='verso'>foo</ab><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-pb",
            "<body><pb n='1' facs='abcde_1'/><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-gap",
            "<body><gap/><div><p>bar</p></div></body>",
            True,
        ),
        (
            "valid-body-with-multiple-elements",
            """
            <body>
                <pb n="1"/>
                <div><p>bar</p></div>
                <gap/>
                <div><p>bar</p></div>
                <ab type='dorsal' place='verso'>foo</ab>
            </body>
            """,
            True,
        ),
        (
            "invalid-body-with-text-content",
            "<body>foo</body>",
            False,
        ),
        (
            "invalid-body-with-default-content",
            "<body><p>foo</p></body>",
            False,
        ),
        (
            "valid-body-with-bibls",
            """
            <body>
                <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.1-1">SDS VD D 2 5.1-1</ref></bibl>
                <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.2-1">SDS VD D 2 5.2-1</ref></bibl>
                <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.3-1">SDS VD D 2-5.3-1</ref></bibl>
            </body>
            """,
            True,
        ),
        (
            "invalid-body-with-one-bibl",
            """
            <body>
                <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.1-1">SDS VD D 2 5.1-1</ref></bibl>
            </body>
            """,
            False,
        ),
        (
            "invalid-body-with-bibls-and-div",
            """
            <body>
                <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.1-1">SDS VD D 2 5.1-1</ref></bibl>
                <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.2-1">SDS VD D 2 5.2-1</ref></bibl>
                <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.3-1">SDS VD D 2-5.3-1</ref></bibl>
                <div><p>bar</p></div>
            </body>
            """,
            False,
        ),
    ],
)
def test_body(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("body", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-body-with-div-inside-transcription",
            "<text type='transcript'><body><div><p>bar</p></div></body></text>",
            True,
        ),
        (
            "invalid-body-with-bibl-inside-transcription",
            """<text type="transcript">
                <body>
                    <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.1-1">SDS VD D 2 5.1-1</ref></bibl>
                    <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.2-1">SDS VD D 2 5.2-1</ref></bibl>
                    <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.3-1">SDS VD D 2-5.3-1</ref></bibl>
                </body>
            </text>""",
            False,
        ),
        (
            "valid-body-with-bibl-inside-collection",
            """<text type="collection">
                <body>
                    <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.1-1">SDS VD D 2 5.1-1</ref></bibl>
                    <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.2-1">SDS VD D 2 5.2-1</ref></bibl>
                    <bibl><ref target="urn:ssrq:SDS-VD-D_2-5.3-1">SDS VD D 2-5.3-1</ref></bibl>
                </body>
            </text>""",
            True,
        ),
        (
            "invalid-body-with-div-inside-collection",
            """<text type="collection">
                <body>
                    <div><p>bar</p></div>
                </body>
            </text>""",
            False,
        ),
    ],
)
def test_body_constraints(
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

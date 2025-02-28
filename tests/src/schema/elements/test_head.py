import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-head",
            "<head>foo</head>",
            True,
        ),
        (
            "valid-head-with-content-default",
            "<head><del>foo</del>bar</head>",
            True,
        ),
        (
            "valid-head-with-p",
            "<head><p>foo</p><p>bar</p></head>",
            True,
        ),
        (
            "valid-head-with-bibl",
            "<head><bibl>foo</bibl></head>",
            True,
        ),
        (
            "valid-head-with-seg",
            "<head><seg>foo</seg><seg>bar</seg></head>",
            True,
        ),
        (
            "invalid-head-with-just-one-seg",
            "<head><seg>foo</seg></head>",
            False,
        ),
        (
            "valid-head-with-type",
            "<head type='title'>foo</head>",
            True,
        ),
        (
            "valid-head-with-place",
            "<head place='above'>foo</head>",
            True,
        ),
        (
            "valid-head-with-resp",
            "<head resp='CS'>foo</head>",
            True,
        ),
        (
            "valid-head-with-n",
            "<head n='1'>foo</head>",
            True,
        ),
        (
            "valid-head-with-xml-lang",
            "<head xml:lang='de'>foo</head>",
            True,
        ),
        (
            "valid-head-with-hand",
            "<head hand='otherHand'>foo</head>",
            True,
        ),
    ],
)
def test_head_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("head", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-head-in-msDesc-with-wrong-attributes",
            """
            <msDesc>
                <head hand="firstHand" n="1" place="above" resp="CS" type="title">foo</head>
                <physDesc>
                    <objectDesc>
                        <supportDesc>
                            <support>
                                <material type="paper"/>
                            </support>
                        </supportDesc>
                    </objectDesc>
                    <handDesc>
                        <handNote xml:id='firstHand'/>
                    </handDesc>
                </physDesc>
                <history>
                    <origin>
                        <origDate calendar="gregorian" type="document" when-custom="1000-01-01"/>
                    </origin>
                </history>
            </msDesc>
            """,
            False,
        ),
    ],
)
def test_head_constraints(
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

import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-seal-empty",
            "<seal n='1' condition='absent'/>",
            True,
        ),
        (
            "valid-seal-with-persName",
            """
            <seal n='1' condition='absent'>
                <persName>foo</persName>
            </seal>
            """,
            True,
        ),
        (
            "invalid-seal-with-multiple-persNames",
            """
            <seal n='1' condition='absent'>
                <persName>foo</persName>
                <persName>bar</persName>
            </seal>
            """,
            False,
        ),
        (
            "valid-seal-with-orgName",
            """
            <seal n='1' condition='absent'>
                <orgName>foo</orgName>
            </seal>
            """,
            True,
        ),
        (
            "invalid-seal-with-multiple-orgNames",
            """
            <seal n='1' condition='absent'>
                <orgName>foo</orgName>
                <orgName>bar</orgName>
            </seal>
            """,
            False,
        ),
        (
            "invalid-seal-with-persName-and-orgName",
            """
            <seal n='1' condition='absent'>
                <persName>foo</persName>
                <orgName>bar</orgName>
            </seal>
            """,
            False,
        ),
        (
            "valid-seal-with-p",
            """
            <seal n='1' condition='absent'>
                <p>foo</p>
            </seal>
            """,
            True,
        ),
        (
            "invalid-seal-with-multiple-ps",
            """
            <seal n='1' condition='absent'>
                <p>foo</p>
                <p>bar</p>
            </seal>
            """,
            False,
        ),
        (
            "valid-seal-with-persName-and-p",
            """
            <seal n='1' condition='absent'>
                <persName>foo</persName>
                <p>bar</p>
            </seal>
            """,
            True,
        ),
        (
            "valid-seal-with-wrong-order",
            """
            <seal n='1' condition='absent'>
                <p>bar</p>
                <persName>foo</persName>
            </seal>
            """,
            False,
        ),
        (
            "invalid-seal-without-n",
            "<seal condition='absent'/>",
            False,
        ),
        (
            "invalid-seal-with-wrong-n",
            "<seal n='0' condition='absent'/>",
            False,
        ),
        (
            "invalid-seal-without-condition",
            "<seal n='1'/>",
            False,
        ),
        (
            "valid-seal-with-place",
            "<seal n='1' condition='absent' place='end'/>",
            True,
        ),
        (
            "valid-seal-with-shape",
            "<seal n='1' condition='absent' shape='oval'/>",
            True,
        ),
        (
            "valid-seal-with-material",
            "<seal n='1' condition='absent' material='wax'/>",
            True,
        ),
        (
            "valid-seal-with-facs",
            "<seal n='1' condition='absent' facs='1r'/>",
            True,
        ),
        (
            "valid-seal-with-attachment",
            "<seal n='1' condition='absent' attachment='applied'/>",
            True,
        ),
        (
            "invalid-seal-with-contemporary",
            "<seal n='1' condition='absent' contemporary='true'/>",
            False,
        ),
        (
            "valid-seal-with-db-reference",
            "<seal n='1' condition='absent' ref='https://link-to-a-database.ch/123456'/>",
            True,
        ),
    ],
)
def test_seal(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("seal", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-seal-with-wrong-n",
            """
            <sealDesc>
                <seal n="2" condition="absent"/>
            </sealDesc>
            """,
            False,
        ),
        (
            "invalid-seal-with-wrong-numbering",
            """
            <sealDesc>
                <seal n="2" condition="absent"/>
                <seal n="1" condition="absent"/>
            </sealDesc>
            """,
            False,
        ),
        (
            "valid-seal-with-correct-numbering",
            """
            <sealDesc>
                <seal n="1" condition="absent"/>
                <seal n="2" condition="absent"/>
            </sealDesc>
            """,
            True,
        ),
    ],
)
def test_seal_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

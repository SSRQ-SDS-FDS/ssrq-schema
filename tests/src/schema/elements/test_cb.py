import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-cb-without-n-attribute",
            "<cb/>",
            False,
        ),
        (
            "valid-cb-with-n-attribute",
            "<cb n='a'/>",
            True,
        ),
        (
            "invalid-cb-with-wrong-attribute-value",
            "<cb n='1'/>",
            False,
        ),
        (
            "invalid-cb-with-wrong-attribute",
            "<cb n='a' break='foo'/>",
            False,
        ),
        (
            "invalid-cb-with-content",
            "<cb n='a'>Foo</cb>",
            False,
        ),
    ],
)
def test_cb(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("cb", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-cbs",
            """
            <body>
                <div>
                    <list>
                        <cb n='a'/>
                        <item>foo</item>
                        <cb n='b'/>
                        <item>bar</item>
                    </list>
                </div>
            </body>
            """,
            True,
        ),
        (
            "invalid-cbs-with-same-value",
            """
            <body>
                <div>
                    <list>
                        <cb n='a'/>
                        <item>foo</item>
                        <cb n='a'/>
                        <item>bar</item>
                    </list>
                </div>
            </body>
            """,
            False,
        ),
        (
            "invalid-cbs-with-b-starting",
            """
            <body>
                <div>
                    <list>
                        <cb n='b'/>
                        <item>foo</item>
                        <cb n='a'/>
                        <item>bar</item>
                        <cb n='b'/>
                    </list>
                </div>
            </body>
            """,
            False,
        ),
        (
            "foo",
            """<div>
                <pb n="1r" facs="abc1v"/>
                <list>
                    <cb n="a"/>
                    <item>foo</item>
                    <item>bar</item>
                </list>
                <cb n="a"/>
                <cb n="b"/>
            </div>""",
            False,
        ),
        (
            "invalid-lonely-cb",
            """
            <body>
                <div>
                    <list>
                        <cb n='a'/>
                        <item>foo</item>
                        <item>bar</item>
                    </list>
                </div>
            </body>
            """,
            False,
        ),
    ],
)
def test_cb_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

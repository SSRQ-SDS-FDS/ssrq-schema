import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origin-with-one-origDate",
            """
            <origin>
                <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
            </origin>
            """,
            True,
        ),
        (
            "valid-origin-with-two-origDates",
            """
            <origin>
                <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                <origDate type='content' when-custom='1366-06-29' calendar='gregorian'/>
            </origin>
            """,
            True,
        ),
        (
            "invalid-origin-with-more-than-two-dates",
            """
            <origin>
               <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
               <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
               <origDate type='content' when-custom='1366-06-29' calendar='gregorian'/>
            </origin>
            """,
            False,
        ),
        (
            "invalid-origin-without-origDate",
            """
            <origin>
                <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
            </origin>
            """,
            False,
        ),
        (
            "valid-origin-with-origPlace",
            """
            <origin>
               <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
               <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
            </origin>
            """,
            True,
        ),
        (
            "valid-origin-with-multiple-origPlaces",
            """
            <origin>
               <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
               <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
               <origPlace type='document' ref='loc000651'>Genf</origPlace>
            </origin>
            """,
            True,
        ),
        (
            "valid-origin-with-orgName",
            """
            <origin>
               <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
               <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
               <orgName>Foo</orgName>
            </origin>
            """,
            True,
        ),
        (
            "invalid-origin-with-lang",
            """
            <origin xml:lang='de'>
               <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
               <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
            </origin>
            """,
            False,
        ),
        (
            "invalid-origin-with-wrong-order-of-children",
            """<origin>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                </origin>""",
            False,
        ),
    ],
)
def test_origin_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("origin", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origin-with-two-dates-of-different-types",
            """
                <origin>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origDate type='content' when-custom='1366-06-29' calendar='gregorian'/>
                </origin>
                """,
            True,
        ),
        (
            "invalid-origin-with-two-dates-of-the-same-type",
            """
            <origin>
               <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
               <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
            </origin>
            """,
            False,
        ),
    ],
)
def test_ref_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

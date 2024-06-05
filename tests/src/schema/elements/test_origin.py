import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origin-with-multiple-children",
            """<origin>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origDate type='content' when-custom='1000-01-12' calendar='gregorian'/>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                   <origPlace type='content' ref='loc123456'>Wuppertal</origPlace>
                   <orgName role="issuer" ref="org123456">Kleiner Rat</orgName>
                </origin>""",
            True,
        ),
        (
            "valid-origin-with-lang",
            """<origin xml:lang='de'>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                </origin>""",
            True,
        ),
        (
            "invalid-origin-with-note",
            """<origin>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                   <note>some text</note>
                </origin>""",
            False,
        ),
        (
            "invalid-origin-with-wrong-order-of-child",
            """<origin>
                   <origPlace type='document' ref='loc000650'>Rheineck</origPlace>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                </origin>""",
            False,
        ),
        (
            "invalid-origin-with-more-than-two-dates",
            """<origin>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origDate type='content' when-custom='1366-06-29' calendar='gregorian'/>
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
            "invalid-origin-with-two-dates-of-the-same-type",
            """<origin>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                </origin>""",
            False,
        ),
        (
            "valid-origin-with-two-dates-of-different-types",
            """<origin>
                   <origDate type='document' when-custom='1366-06-29' calendar='gregorian'/>
                   <origDate type='content' when-custom='1366-06-29' calendar='gregorian'/>
                </origin>""",
            True,
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

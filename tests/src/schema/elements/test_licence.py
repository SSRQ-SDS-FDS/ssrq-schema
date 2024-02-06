import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-licence",
            """<licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>
                    Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
                    </licence>""",
            True,
        ),
        (
            "licence-with-invalid-text",
            """<licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>
                    Attribution-NonCommercial-ShareAlike 4.0 International
                    </licence>""",
            False,
        ),
        (
            "invalid-licence",
            "<licence target='licence.bar'>foo bar</licence>",
            False,
        ),
    ],
)
def test_licence(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("licence", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-licence",
            "<licence target='http://licence.bar'/>",
            False,
        ),
    ],
)
def test_licence_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

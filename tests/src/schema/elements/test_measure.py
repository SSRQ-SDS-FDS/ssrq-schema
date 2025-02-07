import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-measure-with-text-content",
            "<measure type='age' unit='year' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "valid-measure-with-content-critical",
            "<measure type='age' unit='year' quantity='1'><del>Foo</del> bar</measure>",
            True,
        ),
        (
            "valid-measure-with-content-display",
            "<measure type='age' unit='year' quantity='1'>Foo <lb/> bar</measure>",
            True,
        ),
        (
            "valid-measure-with-content-content",
            "<measure type='age' unit='year' quantity='1'><num value='1'>Foo</num> bar</measure>",
            True,
        ),
        (
            "valid-measure-with-content-entities",
            """
            <measure type='age' unit='year' quantity='1'>
                <placeName ref='loc123456'>Foo</placeName> bar
            </measure>
            """,
            True,
        ),
        (
            "invalid-measure-without-type",
            "<measure unit='year' quantity='1'>Foo</measure>",
            False,
        ),
        (
            "invalid-measure-without-quantity",
            "<measure type='age' unit='year'>Foo</measure>",
            False,
        ),
        (
            "invalid-measure-without-unit",
            "<measure type='age' quantity='1'>Foo</measure>",
            False,
        ),
        (
            "valid-measure-with-origin",
            "<measure type='currency' origin='BE' unit='fl' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "valid-measure-with-commodity",
            "<measure type='volume' commodity='wheat' unit='Fuder' quantity='1'>Foo</measure>",
            True,
        ),
    ],
)
def test_measure(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("measure", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-measure-with-type-age",
            "<measure type='age' unit='year' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "invalid-measure-with-type-age",
            "<measure type='age' unit='Fuder' quantity='1'>Foo</measure>",
            False,
        ),
        (
            "valid-measure-with-type-area",
            "<measure type='area' unit='Hube' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "invalid-measure-with-type-area",
            "<measure type='area' unit='year' quantity='1'>Foo</measure>",
            False,
        ),
        (
            "valid-measure-with-type-currency",
            "<measure type='currency' unit='fl' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "invalid-measure-with-type-currency",
            "<measure type='currency' unit='year' quantity='1'>Foo</measure>",
            False,
        ),
        (
            "valid-measure-with-type-length",
            "<measure type='length' unit='Elle' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "valid-measure-with-type-length-cm",
            "<measure type='length' unit='cm' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "invalid-measure-with-type-length",
            "<measure type='length' unit='year' quantity='1'>Foo</measure>",
            False,
        ),
        (
            "valid-measure-with-type-undefined",
            "<measure type='undefined' unit='Dutzend' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "invalid-measure-with-type-length",
            "<measure type='undefined' unit='year' quantity='1'>Foo</measure>",
            False,
        ),
        (
            "valid-measure-with-type-volume",
            "<measure type='volume' unit='Becher' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "invalid-measure-with-type-length",
            "<measure type='volume' unit='year' quantity='1'>Foo</measure>",
            False,
        ),
        (
            "valid-measure-with-type-weight",
            "<measure type='weight' unit='Pfund' quantity='1'>Foo</measure>",
            True,
        ),
        (
            "invalid-measure-with-type-weight",
            "<measure type='weight' unit='year' quantity='1'>Foo</measure>",
            False,
        ),
    ],
)
def test_measure_constraints(
    main_constraints: str,
    writer: SimpleTEIWriter,
    name: str,
    markup: str,
    result: bool,
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "repository-valid-de",
            "<repository xml:lang='de'>Staatsarchiv Schwyz</repository>" "",
            True,
        ),
        (
            "repository-valid-fr",
            "<repository xml:lang='fr'>Archives de l’État de Fribourg</repository>" "",
            True,
        ),
        (
            "repository-invalid-lang",
            "<repository xml:lang='it'>Archives de l’État de Fribourg</repository>" "",
            False,
        ),
        (
            "repository-invalid-attr",
            "<repository xml:lang='fr' n='123'>Archives de l’État de Fribourg</repository>",
            False,
        ),
        (
            "invalid-repository-with-non-text-content",
            "<repository xml:lang='fr'><p>Archives de l’État de Fribourg</p></repository>",
            False,
        ),
    ],
)
def test_repository(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("repository", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-empty-repository",
            "<repository xml:lang='de'/>",
            False,
        ),
    ],
)
def test_repository_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

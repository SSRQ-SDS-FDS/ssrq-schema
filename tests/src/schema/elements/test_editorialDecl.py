import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-editorialDecl-with-p",
            "<editorialDecl><p><ref target='https://p.ssrq-sds-fds.ch/guidelines/transcription'/></p></editorialDecl>",
            True,
        ),
        (
            "invalid-editorialDecl-without-p",
            "<editorialDecl/>",
            False,
        ),
        (
            "invalid-editorialDecl-with-attribute",
            "<editorialDecl xml:id='foo'><p><ref target='https://p.ssrq-sds-fds.ch/guidelines/transcription'/></p></editorialDecl>",
            False,
        ),
    ],
)
def test_editorialDecl_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("editorialDecl", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-editorialDecl-content",
            "<editorialDecl><p><ref target='https://p.ssrq-sds-fds.ch/guidelines/transcription'/></p></editorialDecl>",
            True,
        ),
        (
            "invalid-editorialDecl-content",
            "<editorialDecl><p>foo</p></editorialDecl>",
            False,
        ),
    ],
)
def test_editorialDecl_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

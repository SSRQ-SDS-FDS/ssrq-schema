import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)
from saxonche import PySaxonProcessor

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "idno-archive-valid",
            "<idno xml:lang='de' source='http://foo.bar'>foo 123</idno>",
            True,
        ),
        (
            "idno-archive-invalid",
            "<idno xml:lang='de' source='http://foo.bar http://foo.bar'>foo 123</idno>",
            False,
        ),
        (
            "invalid-idno-with-whitespace-only",
            "<idno> </idno>",
            False,
        ),
        (
            "invalid-empty-idno",
            "<idno/>",
            False,
        ),
        (
            "idno-archive-invalid",
            " <idno xml:lang='de' source='foo.bar'>foo</idno>",
            False,
        ),
    ],
)
def test_idno(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("idno", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-series-idno",
            "<seriesStmt><idno>SSRQ-SG-III_4-77-1</idno></seriesStmt>",
            True,
        ),
        (
            "valid-series-idno",
            "<seriesStmt><idno type='uuid'>73988c1a-40e1-4527-94b7-736d418b29d0</idno></seriesStmt>",
            True,
        ),
        (
            "invalid-series-idno",
            "<seriesStmt><idno>73988c1a-40e1-4527-94b7-736d418b29d0</idno></seriesStmt>",
            False,
        ),
    ],
)
def test_series_idno_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-ms-idno",
            "<msIdentifier><idno xml:lang='de'>bar</idno><repository xml:lang='de'>bar</repository></msIdentifier>",
            True,
        ),
        (
            "invalid-ms-idno",
            "<msIdentifier><idno>bar</idno></msIdentifier>",
            False,
        ),
    ],
)
def test_msIdent_idno_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    with PySaxonProcessor(license=False) as proc:
        xp = proc.new_xpath_processor()
        xml = reports[0].report
        node = proc.parse_xml(xml_text=xml)
        xp.set_context(xdm_item=node)
        item = xp.evaluate_single(
            '//*:text[contains(normalize-space(.), "idno element needs")]'
        )
        assert bool(item) is not result

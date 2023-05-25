import pytest
from pyschval.main import (
    SchematronResult,
    validate_chunk,
)

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-precision",
            "<precision precision='low' match='@to-custom'/>",
            True,
        ),
        (
            "valid-precision",
            "<precision precision='low' match='@notBefore-custom @notAfter-custom'/>",
            True,
        ),
        (
            "valid-precision-with-multiple-match-values",
            "<precision precision='low' match='@from-custom @to-custom'/>",
            True,
        ),
        (
            "valid-precision-with-invalid-match-value",
            "<precision precision='low' match='@from-custom@to-custom'/>",
            False,
        ),
        (
            "valid-precision-with-invalid-precision",
            "<precision precision='0.5' match='@to-custom'/>",
            False,
        ),
        (
            "invalid-precision-with-missing-precision",
            "<precision match='@to-from'/>",
            False,
        ),
        (
            "invalid-precision-with-missing-match",
            "<precision precision='medium'/>",
            False,
        ),
    ],
)
def test_precision(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("precision", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-precision-match",
            "<date datingMethod='gregorian' when-custom='1637-10-18'>1637 [Oktober 18]<precision precision='low' match='@when-custom'/></date>",
            True,
        ),
        (
            "multiple-valid-precision-match",
            "<date datingMethod='gregorian' notBefore-custom='1637' notAfter-custom='1703'>nach 1638<precision precision='high' match='@notBefore-custom @notAfter-custom'/></date>",
            True,
        ),
        (
            "invalid-precision-match",
            "<date datingMethod='gregorian' when-custom='1637-10-18'>1637 [Oktober 18]<precision precision='low' match='@when-customs'/></date>",
            False,
        ),
        (
            "invalid-multiple-valid-precision-match",
            "<date datingMethod='gregorian' notBefore-custom='1637' notAfter-custom='1703'>nach 1638<precision precision='high' match='@notBefore-custom @notafter-custom'/></date>",
            False,
        ),
    ],
)
def test_precision_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraints defined for tei:idno."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result

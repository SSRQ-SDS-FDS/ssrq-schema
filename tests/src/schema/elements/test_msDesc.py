import pytest
from pyschval.main import SchematronResult, validate_chunk

from utils.commons import filehandler as io

from ..conftest import (
    TEST_EXAMPLE_DIR,
    RNG_test_function,
    SimpleTEIWriter,
    add_tei_namespace,
)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msDesc",
            "{msDesc}",
            True,
        ),
        (
            "invalid-msDesc",
            "<msDesc><p>foo</p></msDesc>",
            False,
        ),
    ],
)
def test_msDesc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    markup = markup.format(
        msDesc=io.FileHandler.read(directory=TEST_EXAMPLE_DIR, file_name="msDesc.xml")
    )
    test_element_with_rng("msDesc", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msDesc-without-physDesc-with-adminInfo",
            "<msDesc><additional><adminInfo/></additional></msDesc>",
            True,
        ),
        (
            "invalid-msDesc-without-physDesc-and-without-adminInfo",
            "<msDesc></msDesc>",
            False,
        ),
        (
            "valid-msDesc-with-physDesc-and-without-adminInfo",
            "<msDesc><physDesc/></msDesc>",
            True,
        ),
    ],
)
def test_msDesc_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    """Test the constraint, which ensures the usage of tei:adminInfo if tei:physDesc is not used."""
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result

import pytest

from tests.src.schema.conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-datepoint-with-four-digit-year",
            "<date when-custom='1000-01-01' calendar='gregorian'>Foo</date>",
            True,
        ),
        (
            "valid-datepoint-with-dashed-year",
            "<date when-custom='--01-01' calendar='gregorian'>Foo</date>",
            True,
        ),
        (
            "valid-datepoint-with-leading-zero-year",
            "<date when-custom='0900-01-01' calendar='gregorian'>Foo</date>",
            True,
        ),
        (
            "invalid-datepoint-with-three-digit-year",
            "<date when-custom='900-01-01' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "invalid-datepoint-with-five-digit-year",
            "<date when-custom='10001-01-01' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "invalid-datepoint-with-zero-month",
            "<date when-custom='1000-00-01' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "invalid-datepoinbt-with-month-only",
            "<date when-custom='--01' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "invalid-datepoint-with-too-large-month",
            "<date when-custom='1000-13-01' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "valid-datepoint-with-dashed-year-and-month",
            "<date when-custom='---01' calendar='gregorian'>Foo</date>",
            True,
        ),
        (
            "invalid-datepoint-with-dashed--month",
            "<date when-custom='1000--01' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "invalid-datepoint-with-zero-day",
            "<date when-custom='1000-01-00' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "invalid-datepoint-with-too-large-day",
            "<date when-custom='1000-01-32' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "invalid-datepoint-with-year-only",
            "<date when-custom='1000' calendar='gregorian'>Foo</date>",
            False,
        ),
        (
            "date-with-invalid-negative-year",
            "<date when-custom='-1000-01-01' calendar='gregorian'>foo</date>",
            False,
        ),
    ],
)
def test_date_point_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the pattern ssrq.date.point which is used in multiple dating attributes."""

    test_element_with_rng("date", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-timepoint-midnight",
            "<time when-custom='24:00:00'>Foo</time>",
            True,
        ),
        (
            "valid-timepoint-midnight",
            "<time when-custom='00:00:00'>Foo</time>",
            True,
        ),
        (
            "invalid-timepoint-after-midnight",
            "<time when-custom='24:00:01'>Foo</time>",
            False,
        ),
        (
            "valid-timepoint-after-midnight",
            "<time when-custom='00:00:01'>Foo</time>",
            True,
        ),
        (
            "invalid-timepoint-with-one-digit-hour",
            "<time when-custom='1:00:00'>Foo</time>",
            False,
        ),
        (
            "invalid-timepoint-with-one-digit-minute",
            "<time when-custom='00:1:00'>Foo</time>",
            False,
        ),
        (
            "invalid-timepoint-with-one-digit-second",
            "<time when-custom='00:00:1'>Foo</time>",
            False,
        ),
        (
            "invalid-timepoint-with-too-large-hour",
            "<time when-custom='60:00:00'>Foo</time>",
            False,
        ),
        (
            "invalid-timepoint-with-too-large-minute",
            "<time when-custom='00:60:00'>Foo</time>",
            False,
        ),
        (
            "invalid-timepoint-with-too-large-second",
            "<time when-custom='00:00:60'>Foo</time>",
            False,
        ),
    ],
)
def test_time_point_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the pattern ssrq.time.point which is used in multiple attributes for tei:time."""

    test_element_with_rng("time", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        # Tests for ssrq.foliation
        ("valid-foliation-with-recto", "<pb n='r'/>", True),
        ("valid-foliation-with-verso", "<pb n='v'/>", True),
        ("valid-foliation-with-digits", "<pb n='100r'/>", True),
        ("invalid-foliation-with-leading-zero", "<pb n='01r'/>", False),
        ("invalid-foliation-with-zero", "<pb n='0r'/>", False),
        ("valid-foliation-roman", "<pb n='MDCCLXXVIIr'/>", True),
        ("valid-foliation-with-bis", "<pb n='1bisr'/>", True),
        ("valid-foliation-with-a", "<pb n='1ar'/>", True),
        ("invalid-foliation-with-a-and-bis", "<pb n='1abisr'/>", False),
        # Tests for ssrq.pagination
        ("valid-pagination-with-digits", "<pb n='100'/>", True),
        ("invalid-pagination-with-leading-zero", "<pb n='01'/>", False),
        ("invalid-pagination-with-zero", "<pb n='0'/>", False),
        ("valid-pagination-roman", "<pb n='MDCCLXXVII'/>", True),
        ("invalid-pagination-mixed", "<pb n='1XIV'/>", False),
        ("valid-pagination-with-bis", "<pb n='1bis'/>", True),
        ("valid-pagination-with-a", "<pb n='1a'/>", True),
        ("valid-pagination-with-dot", "<pb n='1.32'/>", True),
        ("valid-pagination-cover", "<pb n='cover'/>", True),
        # Tests for ssrq.section
        ("valid-section", "<pb n='s1'/>", True),
        ("invalid-section-with-leading-zero", "<pb n='s01'/>", False),
    ],
)
def test_numbering_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the patterns ssrq.foliation, ssrq.pagination, ssrq.section and ssrq.numbering which
    are used in @n for tei:pb."""

    test_element_with_rng("pb", name, markup, result, False)


# ToDO: Test for ssrq.facs.name
# ToDO: Test for ssrq.pointer.keywords
# ToDO: Test for ssrq.pointer.lemma
# ToDO: Test for ssrq.pointer.org
# ToDO: Test for ssrq.pointer.persons
# ToDO: Test for ssrq.pointer.places
# ToDO: Test for ssrq.pointer.databases
# ToDO: Test for ssrq.pointer.doi
# ToDO: Test for ssrq.pointer.url
# ToDO: Test for ssrq.pointer.urn
# ToDO: Test for ssrq.pointer.target
# ToDO: Test for ssrq.witness.id
# ToDO: Test for ssrq.witness.pointer

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
        (
            "valid-time-duration-one-hour",
            "<time dur-iso='PT1H'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-24-hours",
            "<time dur-iso='PT24H'>Foo</time>",
            True,
        ),
        (
            "invalid-time-duration-25-hours",
            "<time dur-iso='PT25H'>Foo</time>",
            True,
        ),
        (
            "invalid-time-duration-hours-without-leading-zero",
            "<time dur-iso='PT1H'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-one-minute",
            "<time dur-iso='PT1M'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-59-minutes",
            "<time dur-iso='PT59M'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-60-minutes",
            "<time dur-iso='PT60M'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-one-minute-without-leading-zero",
            "<time dur-iso='PT1M'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-one-second",
            "<time dur-iso='PT01S'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-59-seconds",
            "<time dur-iso='PT59S'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-60-seconds",
            "<time dur-iso='PT60S'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-one-second-without-leading-zero",
            "<time dur-iso='PT1S'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-seconds-with-fraction",
            "<time dur-iso='PT01.1234567890S'>Foo</time>",
            True,
        ),
        (
            "invalid-time-duration-seconds-with-fraction-comma",
            "<time dur-iso='PT1,1S'>Foo</time>",
            False,
        ),
        (
            "valid-time-duration-full",
            "<time dur-iso='PT01H01M01.1S'>Foo</time>",
            True,
        ),
        (
            "valid-time-duration-full-repeated",
            "<time dur-iso='R/PT01H01M01.1S'>Foo</time>",
            True,
        ),
    ],
)
def test_time_duration_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the pattern ssrq.time.point which is used in @dur-iso for tei:time."""

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


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-facs-name-with-plica-ending",
            "<pb n='r' facs='Foo_plica'/>",
            True,
        ),
        (
            "valid-facs-name-with-rv-ending1",
            "<pb n='r' facs='Foo_r'/>",
            True,
        ),
        (
            "valid-facs-name-with-rv-ending2",
            "<pb n='r' facs='Foo_v'/>",
            True,
        ),
        (
            "valid-facs-name-with-number_ending",
            "<pb n='r' facs='Foo_100'/>",
            True,
        ),
        (
            "valid-facs-name-with-roman_ending",
            "<pb n='r' facs='Foo_MDCCLXXVII'/>",
            True,
        ),
        (
            "valid-facs-name-with-dashes",
            "<pb n='r' facs='Foo_MDCCLXXVII-1'/>",
            True,
        ),
        (
            "valid-facs-name-with-multiple-values",
            "<pb n='1' facs='Foo_100 Foo_101'/>",
            True,
        ),
        (
            "invalid-facs-name-with-random-ending",
            "<pb n='1' facs='Foo_100u'/>",
            False,
        ),
    ],
)
def test_facs_name_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the pattern ssrq.facs.name which is used in @facs for tei:pb.
    Compare the test for "__" (schematron constraint) in test_constraints.py"""

    test_element_with_rng("pb", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-persons-pointer",
            "<persName ref='per123456'>Foo</persName>",
            True,
        ),
        (
            "valid-persons-pointer-with-letter",
            "<persName ref='per123456a'>Foo</persName>",
            True,
        ),
        (
            "valid-persons-pointer-with-dot",
            "<persName ref='per123456.10'>Foo</persName>",
            True,
        ),
        (
            "valid-persons-pointer-with-letter-and-dot",
            "<persName ref='per123456a.10'>Foo</persName>",
            True,
        ),
        (
            "invalid-persons-pointer-with-five-digits",
            "<persName ref='per12345'>Foo</persName>",
            False,
        ),
        (
            "invalid-persons-pointer-with-seven-digits",
            "<persName ref='per1234567'>Foo</persName>",
            False,
        ),
        (
            "invalid-persons-pointer-with-wrong-letter",
            "<persName ref='per123456d'>Foo</persName>",
            False,
        ),
        (
            "invalid-persons-pointer-with-to-few-digits-after-dot",
            "<persName ref='per123456.1'>Foo</persName>",
            False,
        ),
        (
            "invalid-persons-pointer-with-to-much-digits-after-dot",
            "<persName ref='per123456.100'>Foo</persName>",
            False,
        ),
    ],
)
def test_pointer_person_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the pattern ssrq.pointer.persons which is used for @ref."""

    test_element_with_rng("persName", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-org-pointer",
            "<orgName ref='org123456'>Foo</orgName>",
            True,
        ),
        (
            "invalid-org-pointer-with-letter",
            "<orgName ref='org123456a'>Foo</orgName>",
            False,
        ),
        (
            "valid-org-pointer-with-dot",
            "<orgName ref='org123456.10'>Foo</orgName>",
            True,
        ),
        (
            "invalid-org-pointer-with-five-digits",
            "<orgName ref='org12345'>Foo</orgName>",
            False,
        ),
        (
            "invalid-org-pointer-with-seven-digits",
            "<orgName ref='org1234567'>Foo</orgName>",
            False,
        ),
        (
            "invalid-org-pointer-with-to-few-digits-after-dot",
            "<orgName ref='org123456.1'>Foo</orgName>",
            False,
        ),
        (
            "invalid-org-pointer-with-to-much-digits-after-dot",
            "<orgName ref='org123456.1'>Foo</orgName>",
            False,
        ),
    ],
)
def test_pointer_org_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the pattern ssrq.pointer.org which is used for @ref."""

    test_element_with_rng("orgName", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-places-pointer",
            "<placeName ref='loc123456'>Foo</placeName>",
            True,
        ),
        (
            "invalid-places-pointer-with-letter",
            "<placeName ref='loc123456a'>Foo</placeName>",
            False,
        ),
        (
            "valid-places-pointer-with-dot",
            "<placeName ref='loc123456.10'>Foo</placeName>",
            True,
        ),
        (
            "invalid-places-pointer-with-five-digits",
            "<placeName ref='loc12345'>Foo</placeName>",
            False,
        ),
        (
            "invalid-places-pointer-with-seven-digits",
            "<placeName ref='loc1234567'>Foo</placeName>",
            False,
        ),
        (
            "invalid-places-pointer-with-to-few-digits-after-dot",
            "<placeName ref='loc123456.1'>Foo</placeName>",
            False,
        ),
        (
            "invalid-places-pointer-with-to-much-digits-after-dot",
            "<placeName ref='loc123456.100'>Foo</placeName>",
            False,
        ),
    ],
)
def test_pointer_places_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the pattern ssrq.pointer.places which is used for @ref."""

    test_element_with_rng("placeName", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        # Tests for ssrq.pointer.keywords
        (
            "valid-keyword-pointer",
            "<term ref='key123456'>Foo</term>",
            True,
        ),
        (
            "invalid-keyword-pointer-with-letter",
            "<term ref='key123456a'>Foo</term>",
            False,
        ),
        (
            "valid-keyword-pointer-with-dot",
            "<term ref='key123456.10'>Foo</term>",
            False,
        ),
        (
            "invalid-keyword-pointer-with-five-digits",
            "<term ref='key12345'>Foo</term>",
            False,
        ),
        (
            "invalid-keyword-pointer-with-seven-digits",
            "<term ref='key1234567'>Foo</term>",
            False,
        ),
        # Tests for ssrq.pointer.lemma
        (
            "valid-lemma-pointer",
            "<term ref='lem123456'>Foo</term>",
            True,
        ),
        (
            "invalid-lemma-pointer-with-letter",
            "<term ref='lem123456a'>Foo</term>",
            False,
        ),
        (
            "valid-lemma-pointer-with-dot",
            "<term ref='lem123456.10'>Foo</term>",
            True,
        ),
        (
            "invalid-lemma-pointer-with-five-digits",
            "<term ref='lem12345'>Foo</term>",
            False,
        ),
        (
            "invalid-lemma-pointer-with-seven-digits",
            "<term ref='lem1234567'>Foo</term>",
            False,
        ),
        (
            "invalid-lemma-pointer-with-to-few-digits-after-dot",
            "<term ref='lem123456.1'>Foo</term>",
            False,
        ),
        (
            "invalid-lemma-pointer-with-three-digits-after-dot",
            "<term ref='lem123456.100'>Foo</term>",
            True,
        ),
    ],
)
def test_pointer_keywords_and_lemmata_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    """Test the patterns ssrq.pointer.keywords and ssrq.pointer.lemma which are used for @ref."""

    test_element_with_rng("term", name, markup, result, False)


# ToDo: Add tests for ssrq.pointer.doi
# ToDo: Add tests for ssrq.pointer.url
# ToDo: Add tests for ssrq.pointer.urn
# ToDo: Add tests for ssrq.pointer.target
# ToDo: Add tests for ssrq.witness.id
# ToDo: Add tests for ssrq.witness.pointer

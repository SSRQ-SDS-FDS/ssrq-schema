import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-origDate-without-content",
            "<origDate type='content' calendar='gregorian' when-custom='1000-01-01'/>",
            True,
        ),
        (
            "valid-origDate-with-text-content",
            "<origDate type='content' calendar='gregorian' when-custom='1000-01-01'>bar</origDate>",
            True,
        ),
        (
            "valid-origDate-with-content-default",
            """
            <origDate type='content' calendar='gregorian' when-custom='1000-01-01'>
                <del>foo</del> bar
            </origDate>
            """,
            True,
        ),
        (
            "valid-origDate-with-precision",
            """
            <origDate type='content' calendar='gregorian' when-custom='1000-01-01'>
                <precision match='@when-custom' precision='high'/>
            </origDate>
            """,
            True,
        ),
        (
            "invalid-origDate-with-wrong-content",
            """
            <origDate type='content' calendar='gregorian' when-custom='1000-01-01'>
                <p>foo</p>
            </origDate>
            """,
            False,
        ),
        (
            "invalid-origDate-without-calendar",
            "<origDate type='content' when-custom='1000-01-01'/>",
            False,
        ),
        (
            "invalid-origDate-with-period",
            "<origDate type='content' calendar='gregorian' period='foo' when-custom='1000-01-01'/>",
            False,
        ),
        (
            "invalid-origDate-without-type",
            "<origDate calendar='gregorian' when-custom='1000-01-01'/>",
            False,
        ),
    ],
)
def test_element(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("origDate", name, markup, result, False)

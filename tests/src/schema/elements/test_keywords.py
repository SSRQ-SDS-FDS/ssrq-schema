import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-keywords",
            "<keywords><term ref='key000192'/></keywords>",
            True,
        ),
        (
            "valid-keywords-with-multiple-terms",
            "<keywords><term ref='key000192'/><term ref='key000193'/></keywords>",
            True,
        ),
        (
            "invalid-keywords-with-scheme",
            """
            <keywords scheme='http://www.ssrq-sds-fds.ch/taxonomie'>
                <term ref='key000192'/>
            </keywords>
            """,
            False,
        ),
    ],
)
def test_keywords_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("keywords", name, markup, result, False)

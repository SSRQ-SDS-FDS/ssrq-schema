import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-profileDesc",
            """
            <profileDesc>
                <textClass>
                    <keywords>
                        <term ref='key000192'/>
                    </keywords>
                </textClass>
            </profileDesc>
            """,
            True,
        ),
        (
            "invalid-profileDesc-with-wrong-content",
            "<profileDesc><p>foo</p></profileDesc>",
            False,
        ),
    ],
)
def test_profile_desc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("profileDesc", name, markup, result, False)

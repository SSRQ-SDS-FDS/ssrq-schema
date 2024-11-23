import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-encodingDesc",
            """
            <encodingDesc>
                <editorialDecl>
                    <p>
                        <ref target='https://www.ssrq-sds-fds.ch/wiki/Transkriptionsrichtlinien'/>
                    </p>
                </editorialDecl>
            </encodingDesc>""",
            True,
        ),
    ],
)
def test_encoding_desc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("encodingDesc", name, markup, result, False)

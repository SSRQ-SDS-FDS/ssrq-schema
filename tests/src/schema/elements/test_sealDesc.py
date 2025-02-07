import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sealDesc",
            """
            <sealDesc>
                <seal n='1' condition='absent'/>
            </sealDesc>
            """,
            True,
        ),
        (
            "valid-sealDesc-with-multiple-seals",
            """
            <sealDesc>
                <seal n='1' condition='absent'/>
                <seal n='2' condition='absent'/>
            </sealDesc>
            """,
            True,
        ),
        (
            "invalid-sealDesc-with-wrong-content",
            "<sealDesc><p>foo</p></sealDesc>",
            False,
        ),
    ],
)
def test_seal_desc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("sealDesc", name, markup, result, False)

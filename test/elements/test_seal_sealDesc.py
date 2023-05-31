import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-sealDesc",
            "<sealDesc/>",
            False,
        ),
        (
            "valid-sealDesc-with-valid-seal",
            """
            <sealDesc>
                <seal n="1" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
            </sealDesc>
            """,
            True,
        ),
        (
            "valid-sealDesc-with-invalid-seal",
            """
            <sealDesc>
                <seal n="1" material="wax" shape="round" attachment="sealed on a parchment tag" condition="damaged">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
            </sealDesc>
            """,
            False,
        ),
        (
            "valid-sealDesc-with-invalid-seal-number",
            """
            <sealDesc>
                <seal n="I" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
            </sealDesc>
            """,
            False,
        ),
    ],
)
def test_seal_sealDesc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("sealDesc", name, markup, result, False)

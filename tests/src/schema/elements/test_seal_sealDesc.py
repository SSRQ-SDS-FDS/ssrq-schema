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


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sealDesc-with-valid-seal",
            """
            <sealDesc>
                <seal n="1" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
                <seal n="2" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
            </sealDesc>
            """,
            True,
        ),
        (
            "valid-sealDesc-with-invalid-seal-number",
            """
            <sealDesc>
                <seal n="1" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
                <seal n="1" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
            </sealDesc>
            """,
            False,
        ),
    ],
)
def test_seal_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = validate_chunk(
        files=writer.list(), isosch=main_constraints
    )
    assert reports[0].is_valid() is result

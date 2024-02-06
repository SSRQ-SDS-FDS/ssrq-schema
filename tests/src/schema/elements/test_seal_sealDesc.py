import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

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
        (
            "valid-seal-with-optional-material",
            """
            <sealDesc>
                <seal n="1" shape="round" attachment="sealed_on_a_parchment_tag" condition="absent">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
            </sealDesc>
            """,
            True,
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
                <seal n="3" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
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
                <seal n="2" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
                    <persName role="sigillant" ref="per000271">Johannes von Belmont</persName>
                </seal>
                <seal n="2" material="wax" shape="round" attachment="sealed_on_a_parchment_tag" condition="damaged">
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
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

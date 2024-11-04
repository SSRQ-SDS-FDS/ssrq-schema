import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-ref-with-urn",
            "<ref target='urn:ssrq:SSRQ-ZH-NF_I_2_1-4-1'>SSRQ ZH NF I/2/1 4-1</ref>",
            True,
        ),
        (
            "ref-with-invalid-urn",
            "<ref target='urn:ssrq:SSQ-ZH-NF_I_2_1-4-1'>SSRQ ZH NF I/2/1 4-1</ref>",
            False,
        ),
        (
            "valid-ref-with-external-reference",
            "<ref target='https://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_858'>SSRQ SG III/2, Nr. 231 </ref>",
            True,
        ),
        (
            "valid-ref-with-external-reference-and-hi",
            "<ref target='https://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_858'>SSRQ SG III/2, Nr. <hi rend='sup'>231</hi> </ref>",
            True,
        ),
        (
            "ref-with-invalid-external-reference",
            "<ref target='htt://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_858'>SSRQ SG III/2, Nr. 231 </ref>",
            False,
        ),
    ],
)
def test_ref_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("ref", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-ref-without-target",
            "<ref>abcde</ref>",
            True,
        ),
        (
            "invalid-ref-without-target-and-text",
            "<ref></ref>",
            False,
        ),
        (
            "valid-ref-without-text",
            "<ref target='https://www.ssrq-sds-fds.ch/online/SG_III_2/index.html#p_858'/>",
            True,
        ),
        (
            "invalid-ref-not-in-bibl",
            "<ref target='urn:ssrq:SSRQ-ZH-NF_I_2_1-105-1'>SSRQ ZH NF I/2/1 105-1</ref>",
            False,
        ),
        (
            "valid-ref-in-bibl",
            "<bibl><ref target='urn:ssrq:SSRQ-ZH-NF_I_2_1-105-1'>SSRQ ZH NF I/2/1 105-1</ref></bibl>",
            True,
        ),
    ],
)
def test_ref_constraint(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

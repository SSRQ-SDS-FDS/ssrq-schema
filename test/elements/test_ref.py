from test.conftest import RNG_test_function

import pytest


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

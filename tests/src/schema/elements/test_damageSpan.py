import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "valid-damageSpan",
            "<damageSpan agent='clipping' spanTo='dmg1'/>",
            False,
            "without matching ID",
        ),
        (
            "damageSpan-with-invalid-attribute-values",
            "<damageSpan agent='foo' spanTo='dmg1'/>",
            False,
            "without matching ID",
        ),
        (
            "invalid-damageSpan",
            "<damageSpan agent='clipping' spanTo='dmg1'>foo</damageSpan>",
            False,
            "without matching ID",
        ),
        (
            "damageSpan-with-wrong-attribute",
            "<damageSpan type='bar' agent='clipping' spanTo='dmg1'/>",
            False,
            "without matching ID",
        ),
    ],
)
def test_damageSpan(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("damageSpan", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng(
            "damageSpan", name, markup, result, True
        )
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("damageSpan", name, markup, result, False)

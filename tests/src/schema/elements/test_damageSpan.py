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
        assert validation_result is not None
        reports = [err.message for info in validation_result for err in info.report]
        messages = "".join(reports)
        assert message in messages
    else:
        test_element_with_rng("damageSpan", name, markup, result, False)

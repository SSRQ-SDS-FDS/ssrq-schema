import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "valid-addSpan",
            "<addSpan spanTo='add1'/>",
            False,
            "without matching ID",
        ),
        (
            "valid-addSpan-with-attributes",
            "<addSpan type='sign' hand='otherHand' place='below' rend='other_ink' spanTo='add1'/>",
            False,
            "without matching ID",
        ),
        (
            "addSpan-with-invalid-attribute-values",
            "<addSpan hand='foo' spanTo='add1'/>",
            False,
            None,
        ),
        (
            "invalid-addSpan",
            "<addSpan spanTo='add1'>foo</addSpan>",
            False,
            None,
        ),
    ],
)
def test_addSpan(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("addSpan", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("addSpan", name, markup, result, True)
        assert validation_result is not None
        reports = [err.message for info in validation_result for err in info.report]
        messages = "".join(reports)
        assert message in messages
    else:
        test_element_with_rng("addSpan", name, markup, result, False)

import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "valid-damage-with-add",
            "<damage agent='water'><add hand='otherHand' place='overwritten'>zuͦ trincken</add></damage>",
            True,
            None,
        ),
        (
            "valid-damage-with-gap",
            "<damage agent='faded_ink clipping'><gap quantity='9' unit='cm'/></damage>",
            True,
            None,
        ),
        (
            "valid-damage-with-supplied",
            "<damage agent='water'><supplied source='73988c1a-40e1-4527-94b7-736d418b29d0'>verthruwen</supplied></damage>",
            False,
            "without matching ID",
        ),
        (
            "valid-damage-with-unclear",
            "<damage agent='ink_blot'><unclear>die</unclear></damage>",
            True,
            None,
        ),
        (
            "invalid-damage-without-agent",
            "<damage><unclear>die</unclear></damage>",
            False,
            None,
        ),
        (
            "invalid-damage-with-wrong-attribute",
            "<damage agent='ink_blot' type='foo'><unclear>die</unclear></damage>",
            False,
            None,
        ),
    ],
)
def test_damage(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    test_element_with_rng("damage", name, markup, result, True)
    if message:
        validation_result = test_element_with_rng("damage", name, markup, result, True)
        file_reports = validation_result.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages
    else:
        test_element_with_rng("damage", name, markup, result, False)

import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-damage-with-add",
            """
            <damage agent='water'>
                <add hand='otherHand' place='overwritten'>foo</add>
            </damage>
            """,
            True,
        ),
        (
            "valid-damage-with-gap",
            """
            <damage agent='water'>
                <gap quantity='9' unit='cm'/>
            </damage>
            """,
            True,
        ),
        (
            "valid-damage-with-supplied",
            """
            <damage agent='water'>
                <supplied source='id-ssrq-73988c1a-40e1-4527-94b7-736d418b29d0'>
                    foo
                </supplied>
            </damage>""",
            True,
        ),
        (
            "valid-damage-with-unclear",
            """
            <damage agent='ink_blot'>
                <unclear>foo</unclear>
            </damage>
            """,
            True,
        ),
        (
            "valid-damage-with-unit-and-quantity",
            """
            <damage agent='water' unit='character' quantity='3'>
                <unclear>die</unclear>
            </damage>
            """,
            True,
        ),
        (
            "valid-damage-with-gap-and-supplied",
            """
            <damage agent='water'>
                <gap/>
                <supplied resp='MA'>bar</supplied>
            </damage>""",
            True,
        ),
        (
            "valid-damage-with-combination-gap-unclear",
            """
            <damage agent='water'>
                <gap/>
                <unclear>bar</unclear>
            </damage>
            """,
            True,
        ),
        (
            "valid-damage-with-supplied-unclear",
            """
            <damage agent='water'>
                <supplied resp="MA">foo</supplied>
                <unclear>bar</unclear>
            </damage>
            """,
            True,
        ),
        (
            "invalid-damage-without-agent",
            "<damage><unclear>die</unclear></damage>",
            False,
        ),
    ],
)
def test_damage(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("damage", name, markup, result, False)

import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        # Todo: füge diesen Test hinzu, wenn <gi>add</gi> definiert wurde
        #        (
        #          "valid-damage-with-add",
        #            """<damage agent="water spot">
        #                                <add hand="#otherHand" place="overwritten">zuͦ trincken</add>
        #                            </damage>
        #                            """,
        #            True,
        #        ),
        (
            "valid-damage-with-gap",
            """
                                                    <damage agent="water spot">
                                                        <gap quantity="9" unit="cm"/>
                                                    </damage>
                                                """,
            True,
        ),
        (
            "valid-damage-with-supplied",
            """
                                                <damage agent="water spot">
                                                    <supplied source="#73988c1a-40e1-4527-94b7-736d418b29d0">verthruwen</supplied>
                                                </damage>
                                            """,
            True,
        ),
        (
            "valid-damage-with-unclear",
            """
                                    <damage agent="ink blot">
                                        <unclear>die</unclear>
                                    </damage>
                                """,
            True,
        ),
        (
            "invalid-damage-without-agent",
            "<damage><unclear>die</unclear></damage>",
            False,
        ),
        (
            "invalid-damage-with-wrong-attribute",
            "<damage agent='ink blot' type='foo'><unclear>die</unclear></damage>",
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

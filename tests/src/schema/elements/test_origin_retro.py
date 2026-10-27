import pytest

from ..conftest import RNG_test_function

DATE = "<origDate type='content' when-custom='0858-04-16' calendar='julian'>858 April 16</origDate>"

SECOND_DATE = "<origDate type='content' when-custom='0858-04-17' calendar='julian'>858 April 17</origDate>"


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-origin", f"<origin>{DATE}</origin>", True),
        (
            "valid-origin-with-multiple-dates",
            f"<origin>{DATE}{SECOND_DATE}</origin>",
            True,
        ),
        ("invalid-empty-origin", "<origin/>", False),
        (
            "invalid-origin-with-place",
            f"<origin>{DATE}<origPlace type='content'>Zug</origPlace></origin>",
            False,
        ),
    ],
)
def test_origin_retro(
    test_retro_with_rng: RNG_test_function, name: str, markup: str, result: bool
) -> None:
    test_retro_with_rng("origin", name, markup, result, False)

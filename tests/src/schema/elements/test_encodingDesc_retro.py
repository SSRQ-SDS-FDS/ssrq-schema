import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-encoding-desc",
            "<encodingDesc><p>Automatisch erzeugt.</p></encodingDesc>",
            True,
        ),
        ("invalid-empty-encoding-desc", "<encodingDesc/>", False),
        (
            "invalid-editorial-decl",
            "<encodingDesc><editorialDecl><p>foo</p></editorialDecl></encodingDesc>",
            False,
        ),
    ],
)
def test_encoding_desc_retro(
    test_retro_with_rng: RNG_test_function, name: str, markup: str, result: bool
) -> None:
    test_retro_with_rng("encodingDesc", name, markup, result, False)

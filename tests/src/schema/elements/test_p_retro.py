import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-p", "<p>Automatisch erzeugt.</p>", True),
        ("valid-multiline-p", "<p>Metadaten automatisch\nübernommen.</p>", True),
        ("invalid-empty-p", "<p/>", False),
        ("invalid-whitespace-p", "<p> \n\t </p>", False),
        ("invalid-p-with-child", "<p><hi>Automatisch erzeugt.</hi></p>", False),
    ],
)
def test_p_retro(
    test_retro_with_rng: RNG_test_function, name: str, markup: str, result: bool
) -> None:
    test_retro_with_rng("p", name, markup, result, False)

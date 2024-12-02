import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-repository-de",
            "<repository xml:lang='de'>Staatsarchiv Schwyz</repository>",
            True,
        ),
        (
            "valid-repository-fr",
            "<repository xml:lang='fr'>Archives de l’État de Fribourg</repository>",
            True,
        ),
        (
            "invalid-repository-it",
            "<repository xml:lang='it'>Archives de l’État de Fribourg</repository>",
            False,
        ),
        (
            "invalid-repository-with-non-text-content",
            "<repository xml:lang='fr'><p>Archives de l’État de Fribourg</p></repository>",
            False,
        ),
        (
            "invaldi-repository-without-xml-lang",
            "<repository>Staatsarchiv Schwyz</repository>",
            False,
        ),
    ],
)
def test_repository(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("repository", name, markup, result, False)

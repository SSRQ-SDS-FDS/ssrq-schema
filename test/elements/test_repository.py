from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "repository-valid-de",
            "<repository xmlns='http://www.tei-c.org/ns/1.0' xml:lang='de'>Staatsarchiv Schwyz</repository>"
            "",
            True,
        ),
        (
            "repository-valid-fr",
            "<repository xmlns='http://www.tei-c.org/ns/1.0' xml:lang='fr'>Archives de l’État de Fribourg</repository>"
            "",
            True,
        ),
        (
            "repository-invalid-lang",
            "<repository xmlns='http://www.tei-c.org/ns/1.0' xml:lang='it'>Archives de l’État de Fribourg</repository>"
            "",
            False,
        ),
        (
            "repository-invalid-attr",
            "<repository xmlns='http://www.tei-c.org/ns/1.0' xml:lang='fr' n='123'>Archives de l’État de Fribourg</repository>"
            "",
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

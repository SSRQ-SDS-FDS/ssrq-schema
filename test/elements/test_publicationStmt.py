import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-publicationStmt-without-date",
            "<publicationStmt><publisher>SSRQ-SDS-FDS</publisher><availability><p xml:id='facs'>Bibliothèque publique et universitaire de Neuchâtel (BPUN)</p><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability></publicationStmt>",
            True,
        ),
        (
            "valid-publicationStmt-with-date",
            "<publicationStmt><publisher>SSRQ-SDS-FDS</publisher><date when-custom='2020-03-03' type='electronic'/><availability><p xml:id='facs'>Bibliothèque publique et universitaire de Neuchâtel (BPUN)</p><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability></publicationStmt>",
            True,
        ),
        (
            "invalid-publicationStmt-without-publisher",
            "<publicationStmt><availability><p xml:id='facs'>Bibliothèque publique et universitaire de Neuchâtel (BPUN)</p><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability></publicationStmt>",
            False,
        ),
    ],
)
def test_publicationStmt_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("publicationStmt", name, markup, result, False)

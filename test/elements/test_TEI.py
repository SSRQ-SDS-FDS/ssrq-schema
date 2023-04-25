from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result, message",
    [
        (
            "TEI-valid",
            """<TEI xml:lang='de'><teiHeader><fileDesc><titleStmt><title>foo</title>
            </titleStmt><publicationStmt><publisher>SSRQ-SDS-FDS</publisher><availability><p xml:id='facs'>Bibliothèque publique et universitaire de Neuchâtel (BPUN)</p><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial- ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability></publicationStmt><sourceDesc><p>foo</p></sourceDesc></fileDesc>
            </teiHeader><text><body></body></text></TEI>""",
            True,
            None,
        ),
        (
            "TEI-invalid-content",
            "<TEI xml:lang='de'><teiHeader></teiHeader><facsimile></facsimile><text></text></TEI>",
            False,
            None,
        ),
        (
            "TEI-invalid-att",
            " <TEI xml:lang='fr' n='1234'><teiHeader></teiHeader><text></text></TEI>",
            False,
            'attribute "n" not allowed here',
        ),
        (
            "TEI-invalid-lang",
            " <TEI xml:lang='pt'><teiHeader></teiHeader><text></text></TEI>",
            False,
            'must be equal to "de", "fr" or "it"',
        ),
    ],
)
def test_TEI_main_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
    message: str | None,
):
    rng_test = test_element_with_rng("TEI", name, markup, result, True)
    if message is not None and rng_test is not None:
        file_reports = rng_test.reports[0]
        assert isinstance(file_reports.report, list)
        messages = "".join([error.message for error in file_reports.report])
        assert message in messages

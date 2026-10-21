import pytest

from ..conftest import RNG_test_function

VALID_TEI = """
<TEI xml:lang='de'>
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Grund- und Territorialherren. Stadt und Amt</title>
        <editor><persName>Eugen Gruber</persName></editor>
        <respStmt><persName>Eugen Gruber</persName><resp>Transkription</resp></respStmt>
      </titleStmt>
      <publicationStmt>
        <publisher>SSRQ-SDS-FDS</publisher>
        <date type='electronic' when-custom='2026-09-22'/>
        <date type='print' from-custom='1971-01-01' to-custom='1971-12-31'/>
        <availability><licence target='https://creativecommons.org/licenses/by-nc-sa/4.0/'>Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</licence></availability>
      </publicationStmt>
      <seriesStmt>
        <title>Sammlung Schweizerischer Rechtsquellen</title>
        <idno>SSRQ-ZG-1_1-1-1</idno>
        <idno type='uuid'>d9bf0588-e28a-4b62-ad82-45b95722d684</idno>
      </seriesStmt>
      <sourceDesc>
        <msDesc>
          <head>Schenkung des Hofs Cham an das Kloster Zürich</head>
          <history><origin><origDate type='content' when-custom='0858-04-16' calendar='julian'>858 April 16</origDate></origin></history>
        </msDesc>
      </sourceDesc>
    </fileDesc>
    <encodingDesc><p>Metadaten aus dem retrodigitalisierten Stückverzeichnis automatisch übernommen.</p></encodingDesc>
  </teiHeader>
  <text type='retro'><body><pb type='pdf' n='43' facs='81'/></body></text>
</TEI>
"""


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-retro-tei", VALID_TEI, True),
        (
            "invalid-retro-tei-without-language",
            VALID_TEI.replace(" xml:lang='de'", ""),
            False,
        ),
        (
            "invalid-retro-tei-without-text",
            VALID_TEI.replace(
                "<text type='retro'><body><pb type='pdf' n='43' facs='81'/></body></text>",
                "",
            ),
            False,
        ),
    ],
)
def test_tei_retro(
    test_retro_with_rng: RNG_test_function, name: str, markup: str, result: bool
) -> None:
    test_retro_with_rng("TEI", name, markup, result, True)

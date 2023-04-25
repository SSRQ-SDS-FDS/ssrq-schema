from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sourceDesc",
            """ <sourceDesc>
            <msDesc>
               <msIdentifier><idno xml:lang='de' source='http://foo.bar'>bar</idno><repository xml:lang='de'>foo</repository></msIdentifier>
               <head>Projekt eines Eides für den Förster oder Bannwart in Sax-Forstegg</head>
               <msContents>
                  <summary><p xml:lang='de'>foo</p></summary>
                  <msItem>
                     <textLang xml:lang="de"/>
                     <filiation type="current">Abschrift, Buch (729 Seiten) mit kartoniertem Einband</filiation>
                  </msItem>
               </msContents>
               <physDesc>
                  <objectDesc>
                     <supportDesc>
                        <support>
                           <material type='paper'/>
                        </support>
                        <extent>
                           <dimensions type="leaves">
                              <height unit="cm" quantity="36.0"/>
                              <width unit="cm" quantity="23.5"/>
                           </dimensions>
                        </extent>
                     </supportDesc>
                  </objectDesc>
               </physDesc>
               <history>
                  <origin>
                     <origDate from-custom="1615-04-15" to-custom="1700-12-31"/>
                  </origin>
               </history>
            </msDesc>
         </sourceDesc>""",
            True,
        ),
        (
            "invalid-sourceDesc",
            "<sourceDesc><p>foo</p></sourceDesc>",
            False,
        ),
    ],
)
def test_sourceDesc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("sourceDesc", name, markup, result, False)

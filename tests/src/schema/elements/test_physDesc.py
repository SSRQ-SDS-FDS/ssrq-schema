import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-physDesc",
            """<physDesc>
            <objectDesc>
                     <supportDesc>
                        <support>
                           <material type='paper'/>
                        </support>
                        <extent>
                           <dimensions type="leaves">
                              <height unit="cm" quantity="16.0"/>
                              <width unit="cm" quantity="23.0"/>
                           </dimensions>
                           <dimensions type="plica">
                              <width unit="cm" quantity="4.0"/>
                           </dimensions>
                        </extent>
                     </supportDesc>
                  </objectDesc>
                </physDesc>""",
            True,
        ),
        ("invalid-physDesc", "<physDesc/>", False),
    ],
)
def test_physDesc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("physDesc", name, markup, result, False)

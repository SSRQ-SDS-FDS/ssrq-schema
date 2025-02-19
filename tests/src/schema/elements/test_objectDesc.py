import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-objectDesc",
            """
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
            """,
            True,
        ),
        (
            "objectDesc-with-invalid-attribute-form",
            """
            <objectDesc form='bar'>
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
            """,
            False,
        ),
        (
            "invalid-objectDesc-with-wrong-content",
            "<objectDesc><p>foo</p></objectDesc>",
            False,
        ),
    ],
)
def test_object_desc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("objectDesc", name, markup, result, False)

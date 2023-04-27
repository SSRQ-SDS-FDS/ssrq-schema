from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-witness",
            """<witness xml:id="foo">
                        <msDesc>
                            <msIdentifier>
                                <idno>foo</idno>
                                <repository>bar</repository>
                            </msIdentifier>
                        </msDesc>                            
                    </witness>""",
            True,
        ),
        (
            "witness-with-invalid-attribute",
            """<witness type="foo">
                        <msDesc>
                            <msIdentifier>
                                <idno>foo</idno>
                                <repository>bar</repository>
                            </msIdentifier>
                        </msDesc>                            
                    </witness>""",
            False,
        ),
    ],
)
def test_witness(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("witness", name, markup, result, False)

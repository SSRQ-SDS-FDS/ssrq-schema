import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msIdentifier",
            """<msIdentifier>
                    <repository xml:lang='de'>foo</repository>
                    <idno xml:lang='de' source='http://foo.bar'>bar</idno>
                </msIdentifier>""",
            True,
        ),
        (
            "valid-msIdentifier-with-multiple-altIdentifier",
            """<msIdentifier>
                    <repository xml:lang='de'>foo</repository>
                    <idno xml:lang='de' source='http://foo.bar'>bar</idno>
                    <altIdentifier>
                        <idno>Nr. Bar</idno>
                    </altIdentifier>
                    <altIdentifier>
                        <idno>Nr. Foo</idno>
                    </altIdentifier>
                </msIdentifier>""",
            True,
        ),
        (
            "valid-msIdentifie-with-settlement",
            """<msIdentifier>
                    <settlement ref="loc123456" xml:lang="de">foo</settlement>
                    <repository xml:lang='de'>foo</repository>
                    <idno xml:lang='de' source='http://foo.bar'>bar</idno>
                </msIdentifier>""",
            True,
        ),
        (
            "invalid-msIdentifier-missing-content",
            """<msIdentifier>
                    <repository xml:lang='de'>foo</repository>
                    <idno xml:lang='de' source='http://foo.bar'>bar</idno>
                    <idno xml:lang='fr' source='http://foo.bar'>bar</idno>
                </msIdentifier>""",
            False,
        ),
    ],
)
def test_msIdentifier(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("msIdentifier", name, markup, result, False)

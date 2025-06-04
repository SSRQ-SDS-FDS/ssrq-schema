import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "invalid-msIdentifier-without-settlement",
            """
            <msIdentifier>
                <repository xml:lang='de'>foo</repository>
                <idno xml:lang='de' source='http://foo.bar'>bar</idno>
            </msIdentifier>
            """,
            False,
        ),
        (
            "valid-msIdentifier",
            """
            <msIdentifier>
                <settlement ref="loc123456" xml:lang="de">foo</settlement>
                <repository xml:lang='de'>foo</repository>
                <idno xml:lang='de' source='http://foo.bar'>bar</idno>
            </msIdentifier>
            """,
            True,
        ),
        (
            "valid-msIdentifier-with-multiple-elements",
            """
            <msIdentifier>
                <settlement ref="loc123456" xml:lang="de">foo</settlement>
                <repository xml:lang='de'>foo</repository>
                <idno xml:lang='de' source='http://foo.bar'>bar</idno>
                <settlement ref="loc123456" xml:lang="de">foo</settlement>
                <repository xml:lang='de'>foo</repository>
                <idno xml:lang='de' source='http://foo.bar'>bar</idno>
            </msIdentifier>
            """,
            True,
        ),
        (
            "valid-msIdentifier-with-altIdentifier",
            """<msIdentifier>
                    <settlement ref="loc123456" xml:lang="de">foo</settlement>
                    <repository xml:lang='de'>foo</repository>
                    <idno xml:lang='de' source='http://foo.bar'>bar</idno>
                    <altIdentifier>
                        <idno>Nr. Bar</idno>
                    </altIdentifier>
                </msIdentifier>""",
            True,
        ),
        (
            "valid-msIdentifier-with-multiple-altIdentifiers",
            """<msIdentifier>
                    <settlement ref="loc123456" xml:lang="de">foo</settlement>
                    <repository xml:lang='de'>foo</repository>
                    <idno xml:lang='de' source='http://foo.bar'>bar</idno>
                    <altIdentifier>
                        <idno>Nr. Foo</idno>
                    </altIdentifier>
                    <altIdentifier>
                        <idno>Nr. Bar</idno>
                    </altIdentifier>
                </msIdentifier>""",
            True,
        ),
        (
            "invalid-msIdentifier-missing-content",
            """<msIdentifier>
                    <settlement ref="loc123456" xml:lang="de">foo</settlement>
                    <repository xml:lang='de'>foo</repository>
                    <idno xml:lang='de' source='http://foo.bar'>bar</idno>
                    <idno xml:lang='fr' source='http://foo.bar'>bar</idno>
                </msIdentifier>""",
            False,
        ),
    ],
)
def test_ms_identifier(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("msIdentifier", name, markup, result, False)

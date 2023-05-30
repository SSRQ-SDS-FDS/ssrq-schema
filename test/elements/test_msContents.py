import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msContents-with-summary",
            """
            <msContents>
                <summary>
                    <p>Graf Heinrich II. von Werdenberg-Heiligenberg(-Rheineck) verleiht den Brüdern
                        Konrad, Heinz und Hans Grafer den Zoll von St. Ulrich und die Schenke in
                        Sevelen.</p>
                </summary>
                <msItem>
                    <textLang xml:lang="de"/>
                    <filiation type="current">Original</filiation>
                </msItem>
            </msContents>
            """,
            True,
        ),
        (
            "valid-msContents-without-summary",
            """
            <msContents>
                <msItem>
                    <textLang xml:lang="de"/>
                    <filiation type="current">Original</filiation>
                </msItem>
            </msContents>
            """,
            True,
        ),
        (
            "invalid-msContents-without-msItem",
            """
            <msContents>
                <summary>
                    <p>Graf Heinrich II. von Werdenberg-Heiligenberg(-Rheineck) verleiht den Brüdern
                        Konrad, Heinz und Hans Grafer den Zoll von St. Ulrich und die Schenke in
                        Sevelen.</p>
                </summary>
            </msContents>
            """,
            False,
        ),
    ],
)
def test_element(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("msContents", name, markup, result, False)

import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msContents",
            "<msContents><msItem><textLang xml:lang='de'/></msItem></msContents>",
            True,
        ),
        (
            "valid-msContents-with-summary",
            """
            <msContents>
                <summary xml:lang='de'><p>Foo</p></summary>
                <msItem><textLang xml:lang="de"/></msItem>
            </msContents>
            """,
            True,
        ),
        (
            "invalid-msContents-with-wrong-order",
            """
            <msContents>
                <msItem><textLang xml:lang="de"/></msItem>
                <summary xml:lang='de'><p>Foo</p></summary>
            </msContents>
            """,
            False,
        ),
        (
            "valid-msContents-with-multiple-summaries",
            """
            <msContents>
                <summary xml:lang='de'><p>Foo</p></summary>
                <summary xml:lang='fr'><p>Foo</p></summary>
                <msItem><textLang xml:lang="de"/></msItem>
            </msContents>
            """,
            True,
        ),
        (
            "invalid-msContents-without-msItem",
            """
            <msContents>
                <summary xml:lang='de'><p>Foo</p></summary>
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

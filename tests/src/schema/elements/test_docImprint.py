import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-docImprint",
            """
            <docImprint>
                <pubPlace ref='loc123456'>Bern</pubPlace>
                <publisher>Heidegger</publisher>
            </docImprint>
            """,
            True,
        ),
        (
            "invalid-docImprint-with-wrong-order",
            """
            <docImprint>
                <publisher>Heidegger</publisher>
                <pubPlace ref='loc123456'>Bern</pubPlace>
            </docImprint>
            """,
            False,
        ),
        (
            "valid-docImprint-without-pubPlace",
            "<docImprint><publisher>Heidegger</publisher></docImprint>",
            True,
        ),
        (
            "valid-docImprint-without-publisher",
            "<docImprint><pubPlace ref='loc123456'>Bern</pubPlace></docImprint>",
            True,
        ),
        (
            "valid-docImprint-with-multiple-places",
            """
            <docImprint>
                <pubPlace ref='loc123456'>Bern</pubPlace>
                <pubPlace ref='loc123457'>St. Gallen</pubPlace>
                <publisher>Heidegger</publisher>
            </docImprint>""",
            True,
        ),
    ],
)
def test_doc_imprint(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("docImprint", name, markup, result, False)

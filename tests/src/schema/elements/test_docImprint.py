import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-docImprint",
            "<docImprint><pubPlace>Bern</pubPlace><publisher>Heidegger</publisher></docImprint>",
            True,
        ),
        (
            "invalid-empty-docImprint",
            "<docImprint></docImprint>",
            False,
        ),
        (
            "invalid-docImprint-with-attribute",
            "<docImprint type='foo'><pubPlace>Bern</pubPlace><publisher>Heidegger</publisher></docImprint>",
            False,
        ),
        (
            "valid-docImprint-without-pubPlace",
            "<docImprint><publisher>Heidegger</publisher></docImprint>",
            True,
        ),
        (
            "valid-docImprint-without-publisher",
            "<docImprint><pubPlace>Bern</pubPlace></docImprint>",
            True,
        ),
        (
            "valid-docImprint-with-multiple-places",
            "<docImprint><pubPlace>Bern</pubPlace><pubPlace>St. Gallen</pubPlace><publisher>Heidegger</publisher></docImprint>",
            True,
        ),
    ],
)
def test_docImprint(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("docImprint", name, markup, result, False)

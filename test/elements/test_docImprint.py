from typing import Callable

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-docImprint",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0'><pubPlace>Bern</pubPlace><publisher>Heidegger</publisher></docImprint>",
            True,
        ),
        (
            "invalid-docImprint-with-attribute",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0' type='foo'><pubPlace>Bern</pubPlace><publisher>Heidegger</publisher></docImprint>",
            False,
        ),
        (
            "invalid-docImprint-without-pubPlace",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0'><publisher>Heidegger</publisher></docImprint>",
            False,
        ),
        (
            "invalid-docImprint-without-publisher",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0'><pubPlace>Bern</pubPlace></docImprint>",
            False,
        ),
        (
            "invalid-docImprint-with-multiple-places",
            "<docImprint xmlns='http://www.tei-c.org/ns/1.0'><pubPlace>Bern</pubPlace><pubPlace>St. Gallen</pubPlace><publisher>Heidegger</publisher></docImprint>",
            False,
        ),
    ],
)
def test_docImprint(
    test_element_with_rng: Callable[[str, str, str, bool], None],
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("docImprint", name, markup, result)

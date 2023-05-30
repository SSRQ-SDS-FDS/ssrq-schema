from test.conftest import RNG_test_function, load_example

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sourceDesc",
            "<sourceDesc>{msDesc}</sourceDesc>",
            True,
        ),
        (
            "invalid-sourceDesc",
            "<sourceDesc><p>foo</p></sourceDesc>",
            False,
        ),
    ],
)
def test_sourceDesc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    markup = markup.format(msDesc=load_example("msDesc.xml"))
    test_element_with_rng("sourceDesc", name, markup, result, False)

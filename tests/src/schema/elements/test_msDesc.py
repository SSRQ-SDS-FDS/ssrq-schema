import pytest

from ..conftest import RNG_test_function, load_example


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msDesc",
            "{msDesc}",
            True,
        ),
        (
            "invalid-msDesc",
            "<msDesc><p>foo</p></msDesc>",
            False,
        ),
    ],
)
def test_msDesc(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    markup = markup.format(msDesc=load_example("msDesc.xml"))
    test_element_with_rng("msDesc", name, markup, result, False)

import pytest

from utils.commons import filehandler as io

from ..conftest import TEST_EXAMPLE_DIR, RNG_test_function


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
    markup = markup.format(
        msDesc=io.FileHandler.read(dir=TEST_EXAMPLE_DIR, file_name="msDesc.xml")
    )
    test_element_with_rng("msDesc", name, markup, result, False)

import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-gap",
            "<gap/>",
            True,
        ),
        (
            "invalid-gap-with-content",
            "<gap>Foo</gap>",
            False,
        ),
        (
            "invalid-gap-with-attribute",
            "<gap source='urn:ssrq:SSRQ-ZH-NF_II_11-74-1#n17.1-17.4'/>",
            False,
        ),
    ],
)
def test_gap_rng(
    test_intro_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_intro_with_rng("gap", name, markup, result, False)

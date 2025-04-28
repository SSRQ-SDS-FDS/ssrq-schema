import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-sourceDesc-with-p",
            """
            <sourceDesc>
                <p>foo</p>
            </sourceDesc>
            """,
            True,
        ),
        (
            "invalid-sourceDesc-without-p",
            "<sourceDesc>foo</sourceDesc>",
            False,
        ),
    ],
)
def test_source_desc_rng(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("sourceDesc", name, markup, result, False)

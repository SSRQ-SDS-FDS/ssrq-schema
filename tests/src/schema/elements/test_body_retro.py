import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-body", "<body><pb type='pdf' n='43' facs='81'/></body>", True),
        ("invalid-empty-body", "<body/>", False),
        (
            "invalid-body-with-two-pages",
            "<body><pb type='pdf' n='43' facs='81'/><pb type='pdf' n='44' facs='82'/></body>",
            False,
        ),
    ],
)
def test_body_retro(
    test_retro_with_rng: RNG_test_function, name: str, markup: str, result: bool
) -> None:
    test_retro_with_rng("body", name, markup, result, False)

import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-pdf-page", "<pb type='pdf' n='43' facs='81'/>", True),
        ("invalid-without-type", "<pb n='43' facs='81'/>", False),
        ("invalid-without-printed-page", "<pb type='pdf' facs='81'/>", False),
        ("invalid-zero-pdf-page", "<pb type='pdf' n='43' facs='0'/>", False),
        ("invalid-facs-name", "<pb type='pdf' n='43' facs='ZG_1_1_81'/>", False),
    ],
)
def test_pb_retro(
    test_retro_with_rng: RNG_test_function, name: str, markup: str, result: bool
) -> None:
    test_retro_with_rng("pb", name, markup, result, False)

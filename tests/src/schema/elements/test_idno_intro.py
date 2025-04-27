import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-idno",
            "<idno>SDS-VD-D_2-1-1</idno>",
            True,
        ),
        (
            "invalid-idno-with-element-content",
            "<idno><p>SDS-VD-D_2-1-1</p></idno>",
            False,
        ),
        (
            "invalid-idno-with-xml-lang",
            "<idno xml:lang='de'>foo</idno>",
            False,
        ),
        (
            "invalid-idno-with-source",
            "<idno source='http://foo.bar'>foo 123</idno>",
            False,
        ),
        (
            "valid-idno-with-type",
            " <idno type='uuid'>d9bf0588-e28a-4b62-ad82-45b95722d684</idno>",
            True,
        ),
    ],
)
def test_idno(
    test_lit_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_lit_with_rng("idno", name, markup, result, False)

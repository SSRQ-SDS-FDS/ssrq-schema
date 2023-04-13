import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-msIdentifier",
            "<msIdentifier><idno xml:lang='de' source='http://foo.bar'>bar</idno><repository xml:lang='de'>foo</repository></msIdentifier>",
            True,
        ),
        (
            "valid-msIdentifie-with-settlement",
            "<msIdentifier><idno xml:lang='de' source='http://foo.bar'>bar</idno><repository xml:lang='de'>foo</repository><settlement>Zürich</settlement></msIdentifier>",
            True,
        ),
        (
            "invalid-msIdentifier-content",
            "<msIdentifier><idno xml:lang='de' source='http://foo.bar'>bar</idno></msIdentifier>",
            False,
        ),
        (
            "invalid-msIdentifier-content",
            "<msIdentifier><idno xml:lang='de' source='http://foo.bar'>bar</idno><repository xml:lang='de'>foo</repository><idno xml:lang='fr' source='http://foo.bar'>bar</idno></msIdentifier>",
            False,
        ),
    ],
)
def test_msIdentifier(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("msIdentifier", name, markup, result, False)

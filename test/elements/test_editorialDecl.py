from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-editorialDecl",
            "<editorialDecl><p><ref target='https://www.ssrq-sds-fds.ch/wiki/Transkriptionsrichtlinien'/></p></editorialDecl>",
            True,
        ),
        (
            "invalid-editorialDecl-without-p",
            "<editorialDecl/>",
            False,
        ),
        (
            "invalid-editorialDecl-with-attribute",
            "<editorialDecl xml:id='foo'><p><ref target='https://www.ssrq-sds-fds.ch/wiki/Transkriptionsrichtlinien'/></p></editorialDecl>",
            False,
        ),
    ],
)
def test_encodingDesc_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("editorialDecl", name, markup, result, False)

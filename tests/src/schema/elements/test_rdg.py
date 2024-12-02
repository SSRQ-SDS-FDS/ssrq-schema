import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-rdg",
            "<rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'>foo</rdg>",
            True,
        ),
        (
            "valid-empty-rdg",
            "<rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d'/>",
            True,
        ),
        (
            "invalid-rdg-without-attribute",
            "<rdg>foo</rdg>",
            False,
        ),
        (
            "valid-rdg-with-different-wit-values",
            """
            <rdg wit="id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#123
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#p123
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#p123-234
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#n123
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#n123-234
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#fol123r
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#fol123v
                      id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#fol123r-124v">bar</rdg>
            """,
            True,
        ),
        (
            "invalid-rdg-with-incorrect-wit-value-1",
            "<rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#s123'>bar</rdg>",
            False,
        ),
        (
            "invalid-rdg-with-incorrect-wit-value-2",
            "<rdg wit='id-ssrq-ad28656b-5c8d-459c-afb4-3e6ddf70810d#fol123'>bar</rdg>",
            False,
        ),
    ],
)
def test_rdg(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("rdg", name, markup, result, False)

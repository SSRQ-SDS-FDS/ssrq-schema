import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-bibl",
            "<bibl>foo</bibl>",
            True,
        ),
        (
            "valid-bibl-with-xml-id",
            "<bibl xml:id='id-ssrq-12345678-1234-4123-8123-123456789012'>foo</bibl>",
            True,
        ),
        (
            "invalid-bibl-with-attr",
            "<bibl type='lit'>foo</bibl>",
            False,
        ),
        (
            "invalid-bibl-with-default-content",
            "<bibl><p>foo</p></bibl>",
            False,
        ),
        (
            "valid-bibl-with-ref",
            "<bibl><ref target='http://zotero.org/groups/5048222/items/M8D9EG5B'/>, S. 93</bibl>",
            True,
        ),
        (
            "valid-bibl-with-pc-and-ref",
            """
            <bibl>
                <ref target='http://zotero.org/groups/5048222/items/M8D9EG5B'/><pc>:</pc> S. 93
            </bibl>""",
            True,
        ),
    ],
)
def test_bibl(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("bibl", name, markup, result, False)

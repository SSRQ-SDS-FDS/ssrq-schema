import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-additional-with-listBibl",
            """
            <additional>
                <listBibl type='literature'><bibl>foo</bibl></listBibl>
            </additional>
            """,
            True,
        ),
        (
            "valid-additional-with-multiple-listBibl",
            """
                <additional>
                    <listBibl type='edition'><bibl>foo</bibl></listBibl>
                    <listBibl type='literature'><bibl>foo</bibl></listBibl>
                </additional>
                """,
            True,
        ),
        (
            "valid-additional-with-adminInfo-and-listBibl",
            """
            <additional>
                <adminInfo>
                    <custodialHist>
                        <custEvent type="lost" notBefore-custom="1858-09-01" calendar="gregorian">
                            Verlust nicht vor Erscheinen der Erstedition des 19. Jahrhunderts.
                        </custEvent>
                    </custodialHist>
                </adminInfo>
                <listBibl type='literature'><bibl>foo</bibl></listBibl>
            </additional>
            """,
            True,
        ),
        (
            "invalid-additional-with-wrong-child-order",
            """
            <additional>
                <listBibl type='literature'><bibl>foo</bibl></listBibl>
                <adminInfo>
                    <custodialHist>
                        <custEvent type="lost" notBefore-custom="1858-09-01" calendar="gregorian">
                            Verlust nicht vor Erscheinen der Erstedition des 19. Jahrhunderts.
                        </custEvent>
                    </custodialHist>
                </adminInfo>
            </additional>
            """,
            False,
        ),
        (
            "invalid-additional-with-attributes",
            """
            <additional att='foo'>
                <listBibl type='literature'><bibl>foo</bibl></listBibl>
            </additional>
            """,
            False,
        ),
        (
            "invalid-empty-additional",
            "<additional/>",
            False,
        ),
    ],
)
def test_additional(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("additional", name, markup, result, False)

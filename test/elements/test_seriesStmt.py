import pytest

from ..conftest import RNG_test_function


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-seriesStmt",
            """<seriesStmt xml:id='ssrq-sds-fds'>
                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
                        <resp>Herausgeberschaft</resp>
                    </respStmt>
                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                    <idno type='uuid'>ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                </seriesStmt>""",
            True,
        ),
        (
            "invalid-seriesStmt-with-missing-title",
            """<seriesStmt xml:id='ssrq-sds-fds'>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
                        <resp>Herausgeberschaft</resp>
                    </respStmt>
                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                    <idno type='uuid'>ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                </seriesStmt>""",
            False,
        ),
        (
            "invalid-seriesStmt-with-one-idno",
            """<seriesStmt xml:id='ssrq-sds-fds'>
                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
                        <resp>Herausgeberschaft</resp>
                    </respStmt>
                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                </seriesStmt>""",
            False,
        ),
        (
            "invalid-seriesStmt-with-wrong-xml-id",
            """<seriesStmt xml:id='foo'>
                    <title>Sammlung Schweizerischer Rechtsquellen</title>
                    <respStmt>
                        <orgName>Rechtsquellenstiftung des Schweizerischen Juristenvereins</orgName>
                        <resp>Herausgeberschaft</resp>
                    </respStmt>
                    <idno>SSRQ-FR-I_2_8-1-1</idno>
                    <idno type='uuid'>ad28656b-5c8d-459c-afb4-3e6ddf70810d</idno>
                </seriesStmt>""",
            False,
        ),
    ],
)
def test_seriesStmt_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("seriesStmt", name, markup, result, False)

import pytest

from ..conftest import RNG_test_function

SERIES_TITLE = "<title>Sammlung Schweizerischer Rechtsquellen</title>"
IDNOS = "<idno>SSRQ-ZG-1_1-1-1</idno><idno type='uuid'>d9bf0588-e28a-4b62-ad82-45b95722d684</idno>"


@pytest.mark.parametrize(
    "name, markup, result",
    [
        ("valid-series-stmt", f"<seriesStmt>{SERIES_TITLE}{IDNOS}</seriesStmt>", True),
        ("invalid-without-title", f"<seriesStmt>{IDNOS}</seriesStmt>", False),
        (
            "invalid-with-one-idno",
            f"<seriesStmt>{SERIES_TITLE}{IDNOS.split('</idno>')[0]}</idno></seriesStmt>",
            False,
        ),
        (
            "invalid-with-responsibility",
            f"<seriesStmt>{SERIES_TITLE}<respStmt><persName>Foo</persName><resp>Transkription</resp></respStmt>{IDNOS}</seriesStmt>",
            False,
        ),
    ],
)
def test_series_stmt_retro(
    test_retro_with_rng: RNG_test_function, name: str, markup: str, result: bool
) -> None:
    test_retro_with_rng("seriesStmt", name, markup, result, False)

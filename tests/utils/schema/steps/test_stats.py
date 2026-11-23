import logging

import pytest

from utils.schema.steps.stats import (
    Stats,
    get_included_elements,
    get_specified_elements,
)


@pytest.fixture
def stats_example() -> str:
    return """
    <moduleRef key="certainty" include="precision"/>
    <moduleRef key="figures" include="cell
    figure    row   table"/>
    <specGrpRef target="elements/precision.xml"/>"""


def test_input_is_output(stats_example: str) -> None:
    stats = Stats()
    assert stats(stats_example) == stats_example


def test_get_included_elements(stats_example: str) -> None:
    assert get_included_elements(stats_example) == [
        "precision",
        "cell",
        "figure",
        "row",
        "table",
    ]


def test_get_specified_elements(stats_example: str) -> None:
    assert get_specified_elements(stats_example) == ["precision"]


def test_stats_logging_error(
    caplog: pytest.LogCaptureFixture, stats_example: str
) -> None:
    caplog.set_level(logging.INFO)

    stats = Stats()
    stats(stats_example)

    assert [(record.levelname, record.message) for record in caplog.records] == [
        ("INFO", "Number of elements included: 5"),
        ("INFO", "Number of elements specified: 1"),
        ("ERROR", "Number of elements not specified: 4"),
        ("ERROR", "Elements not specified: cell, figure, row, table"),
    ]


def test_stats_logging_without_errors(
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level(logging.INFO)

    schema = """
    <moduleRef key="certainty" include="precision"/>
    <specGrpRef target="elements/precision.xml"/>"""

    stats = Stats()
    stats(schema)

    assert [(record.levelname, record.message) for record in caplog.records] == [
        ("INFO", "Number of elements included: 1"),
        ("INFO", "Number of elements specified: 1"),
        ("INFO", "Number of elements not specified: 0"),
    ]

import pytest

from utils.schema.steps.stats import Stats
from utils.schema.steps.step import AbstractStep


@pytest.fixture
def stats_example() -> str:
    return """
    <moduleRef key="certainty" include="precision"/>
    <moduleRef key="figures" include="cell
    figure    row   table"/>
    <specGrpRef target="elements/precision.xml"/>"""


def test_stats_isinstance_of_step() -> None:
    assert isinstance(Stats(), AbstractStep)


def test_input_is_output(stats_example: str) -> None:
    stats = Stats()
    assert stats(stats_example) == stats_example


def test_calc_included_elements(stats_example: str) -> None:
    stats = Stats()
    assert stats.calculate_number_of_included_elements(stats_example) == 5


def test_calc_specified_elements(stats_example: str) -> None:
    stats = Stats()
    assert stats.calculate_number_of_specified_elements(stats_example) == 1


def test_stats_logging(caplog: pytest.LogCaptureFixture, stats_example: str) -> None:
    stats = Stats()
    stats(stats_example)
    records = caplog.records
    test_messages = (
        "Number of elements included: 5",
        "Number of elements not specified: 4",
    )
    for record, test_message in zip(records, test_messages):
        assert record.levelname == "INFO"
        assert test_message in record.message

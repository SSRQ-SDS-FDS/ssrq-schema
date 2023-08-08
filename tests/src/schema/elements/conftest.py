import pytest


@pytest.fixture
def element_schema(
    change_rng_start_per_odd: dict[str, dict[str, str]]
) -> dict[str, str]:
    """A fixture, which returns the main ssrq schema with a modified start element."""
    return change_rng_start_per_odd["TEI_Schema"]

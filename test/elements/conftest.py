import pytest

from main import Schema

from ..conftest import change_rng_start

ELEMENTS = ["cell", "handShift", "idno"]


@pytest.fixture
def element_schema(main_schema: Schema) -> dict[str, str]:
    """A fixture, which returns the main ssrq schema with a modified start element."""
    return {el: change_rng_start(main_schema.rng, el) for el in ELEMENTS}

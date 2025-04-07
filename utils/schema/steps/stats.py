import re
from functools import reduce

from utils.commons.logger import LOGGER
from utils.schema.compile import SPECIFIED_ELEMENTS


class Stats:
    def __call__(self, value: str) -> str:
        elements_included = self.calculate_number_of_included_elements(value)
        elements_specified = self.calculate_number_of_specified_elements(value)

        LOGGER.info(f"Number of elements included: {elements_included}")
        LOGGER.info(f"Number of elements specified: {elements_specified}")
        LOGGER.info(
            f"Number of elements not specified: {elements_included - elements_specified}"
        )

        return value

    def calculate_number_of_included_elements(self, schema: str) -> int:
        included_elements = map(
            lambda includes: re.sub(r"([\s\n\t])+", " ", includes).split(),
            re.findall(r'include="([A-Za-z\s]+)"', schema),
        )

        return reduce(lambda x, y: x + len(y), included_elements, 0)

    def calculate_number_of_specified_elements(self, schema: str) -> int:
        return len(re.findall(SPECIFIED_ELEMENTS, schema))

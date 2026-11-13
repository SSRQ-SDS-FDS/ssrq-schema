import re

from utils.commons.logger import LOGGER
from utils.schema import SPECIFIED_ELEMENTS


def get_included_elements(schema: str) -> list[str]:
    return [
        element
        for includes in re.findall(r'include="([A-Za-z\s]+)"', schema)
        for element in includes.split()
    ]


def get_specified_elements(schema: str) -> list[str]:
    return re.findall(SPECIFIED_ELEMENTS, schema)


class Stats:
    def __call__(self, value: str) -> str:
        included_elements = get_included_elements(value)
        specified_elements = get_specified_elements(value)

        not_specified_elements = [
            element
            for element in included_elements
            if element not in specified_elements
        ]

        LOGGER.info(f"Number of elements included: {len(included_elements)}")
        LOGGER.info(f"Number of elements specified: {len(specified_elements)}")

        if not_specified_elements:
            LOGGER.error(
                f"Number of elements not specified: {len(not_specified_elements)}"
            )
            LOGGER.error(f"Elements not specified: {', '.join(not_specified_elements)}")
        else:
            LOGGER.info("Number of elements not specified: 0")

        return value

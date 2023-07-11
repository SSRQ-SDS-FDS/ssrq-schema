import re
from abc import ABC, abstractmethod

from utils.constants import SPECIFIED_ELEMENTS


class Stats(ABC):
    @staticmethod
    @abstractmethod
    def show_stats(schema: str, name: str) -> None:
        pass


class AnalyzeStats(Stats):
    @staticmethod
    def show_stats(schema: str, name: str) -> None:
        included_elements: list[str] = " ".join(
            re.findall(r'include="(.*)"', schema)
        ).split(" ")
        specified_elements: list[str] = re.findall(SPECIFIED_ELEMENTS, schema)
        print(
            f"Elements included in {name}: {len(included_elements)}\n"
            f"Elements already specified: {len(specified_elements)}\n"
            f"Elements to specify: {len(included_elements) - len(specified_elements)}\n"
        )

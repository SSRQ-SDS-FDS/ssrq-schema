import xml.etree.ElementTree as ET
from pathlib import Path

from utils.docs.specs.base import BaseSpec


class ClassSpec(BaseSpec):
    def __init__(self, element: ET.Element):
        super().__init__(element=element)
        self.odd_type = "classSpec"

    def to_markdown(
        self, lang: str, lang_translations: dict[str, str], path: Path | None = None
    ) -> str | None:
        pass

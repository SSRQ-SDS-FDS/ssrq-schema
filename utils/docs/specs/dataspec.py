import xml.etree.ElementTree as ET
from pathlib import Path

from utils.docs.specs.abstract import ODD_COMP_TYPES


class DataSpec:
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str
    classes: list[str] | None
    module: str | None

    def __init__(self, element: ET.Element):
        self.odd_element = element
        self.odd_type = "dataSpec"
        self.ident = element.attrib["ident"]
        self.module = element.attrib.get("module")
        self.classes = None

    def to_markdown(
        self, lang: str, lang_translations: dict[str, str], path: Path | None = None
    ) -> str | None:
        pass

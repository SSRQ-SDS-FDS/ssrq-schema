import xml.etree.ElementTree as ET
from abc import abstractmethod
from pathlib import Path
from typing import Literal, Protocol, runtime_checkable

ODD_COMP_TYPES = Literal["elementSpec", "classSpec", "dataSpec", "macroSpec"]


@runtime_checkable
class ODDElement(Protocol):
    odd_element: ET.Element
    odd_type: ODD_COMP_TYPES
    ident: str
    module: str | None
    classes: list[str] | None

    @abstractmethod
    def to_markdown(
        self, lang: str, lang_translations: dict[str, str], path: Path | None = None
    ) -> None | str:
        ...

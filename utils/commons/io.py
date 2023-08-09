from abc import abstractmethod
from pathlib import Path
from typing import Protocol, TypeAlias, runtime_checkable

Content: TypeAlias = str


@runtime_checkable
class ReaderWriter(Protocol):
    @staticmethod
    @abstractmethod
    def read(dir: Path, file_name: str) -> Content:
        ...

    @staticmethod
    @abstractmethod
    def write(dir: Path, file_name: str, content: Content) -> None:
        ...


class FileHandler:
    @staticmethod
    def read(dir: Path, file_name: str) -> Content:
        with open(dir / file_name, encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def write(dir: Path, file_name: str, content: Content) -> None:
        from os import makedirs
        from os.path import exists

        if not exists(dir):
            makedirs(dir)

        with open(dir / file_name, "w", encoding="utf-8") as f:
            f.write(content)

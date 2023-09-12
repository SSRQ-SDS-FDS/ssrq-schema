from abc import abstractmethod
from pathlib import Path
from typing import Protocol, TypeAlias, runtime_checkable

Content: TypeAlias = str


@runtime_checkable
class AbstractFileHandler(Protocol):
    @staticmethod
    @abstractmethod
    def read(directory: Path, file_name: str) -> Content:
        ...

    @staticmethod
    @abstractmethod
    def write(directory: Path, file_name: str, content: Content) -> None:
        ...


class FileHandler:
    @staticmethod
    def read(directory: Path, file_name: str) -> Content:
        with open(directory / file_name, encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def write(directory: Path, file_name: str, content: Content) -> None:
        FileHandler.__create_directory_if_not_exists(directory)
        FileHandler.__write_content_to_file(directory, file_name, content)

    @staticmethod
    def __write_content_to_file(directory, file_name, content):
        with open(directory / file_name, "w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def __create_directory_if_not_exists(directory):
        from os import makedirs
        from os.path import exists

        if not exists(directory):
            makedirs(directory)

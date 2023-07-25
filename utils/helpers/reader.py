from typing import Protocol, runtime_checkable


@runtime_checkable
class Reader(Protocol):
    """
    A reader, which has a read method that takes a path and returns a string.
    """

    def read(self, path: str) -> str:
        """
        Read the file at the given path.

        Args:
            path (str): The path to the file to read.

        Returns:
            str: The content of the file.

        """
        ...


class FileReader:
    def read(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

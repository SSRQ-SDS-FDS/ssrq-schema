from typing import Protocol, runtime_checkable


@runtime_checkable
class Step(Protocol):
    """
    A step in the ODD pipeline, which has an apply method that takes a string and returns a string.
    """

    def apply(self, doc: str) -> str:
        """
        Apply the step to the given document.

        Args:
            doc (str): The document to apply the step to.

        Returns:
            str: The document after the step has been applied.

        """
        ...

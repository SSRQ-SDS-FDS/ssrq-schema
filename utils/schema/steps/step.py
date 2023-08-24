from abc import abstractmethod
from typing import Protocol, TypeVar, runtime_checkable

T = TypeVar("T")


@runtime_checkable
class AbstractStep(Protocol):
    """A protocol, which defines the interface for a step
    in a processing pipeline."""

    @abstractmethod
    def __call__(self, value: T) -> T:
        ...

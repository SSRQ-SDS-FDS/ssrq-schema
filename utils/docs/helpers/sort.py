from collections.abc import Callable, Iterable
from typing import TypeVar

from pyuca import Collator  # type: ignore

__all__ = ["sort_with_uca"]

c = Collator()

Item = TypeVar("Item")


def sort_with_uca(
    items: Iterable[Item],
    sort_key: None | Callable[[Item], str] = None,
    reverse: bool = False,
) -> list[Item]:
    """Sort the given items by the unicode collation algorithm.
    This function is just a wrapper around James K. Tauber's pyuca library.
    With this module we just have to pass the items to sort and the function
    without initializing the collator object every time.

    Args:
        items (Iterable[Item]): The items to sort.
        sort_key (None | Callable[[Item], str], optional): A function which returns the
            string used as a key for sorting. Defaults to None.
        reverse (bool, optional): Whether to reverse the order. Defaults to False.

    Returns:
        list[Item]: The sorted items.
    """
    return sorted(
        items,
        key=lambda i: c.sort_key(i) if sort_key is None else c.sort_key(sort_key(i)),
        reverse=reverse,
    )

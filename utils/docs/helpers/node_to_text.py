import re
import xml.etree.ElementTree as ET
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Literal
from urllib import parse

from utils.commons.config import DOCS_LANG
from utils.docs.helpers.utils import split_tag_and_ns
from utils.docs.specs.namespaces import XML_NS

RE_WHITESPACE_START_OR_MULTIPLE = re.compile(
    r"^\s+|\s+$|\s+(?=-\S+)|\s+(?=\s)"
)  # This is a regex to remove whitespace from the start and end of a string,
# and also to remove whitespace before a hyphen and whitespace before a space.


@dataclass(frozen=True)
class Node:
    content: ET.Element | str
    type: Literal["tag", "text", "tail"]
    tag_name: str | None = None


class NodeTransformationError(Exception):
    def __init__(self, message: str = "Can't transform the node.") -> None:
        super().__init__(message)


def transform_node_to_text(node: ET.Element, lang: str | None = None) -> Iterator[str]:
    """
    A utility function to convert an ET.Element node to
    a text representation, based on some opinionated
    transformation rules.

    Args:
        node (ET.Element): The node to convert.
        lang: The language of the node.

    Yields:
        Iterator[str]: The text representation of the node.

    """
    parent_lang_attr = (
        lang_attr if (lang_attr := node.get(f"{{{XML_NS}}}lang")) else lang
    )
    for child_node in convert_node_to_iterable(node):
        if (
            child_node.type == "tag"
            and child_node.tag_name is not None
            and isinstance(child_node.content, ET.Element)
        ):
            used_lang = (
                lang_attr
                if (lang_attr := node.get(f"{{{XML_NS}}}lang"))
                else parent_lang_attr
            )
            yield from match_node_tag_name(child_node, used_lang)
            continue

        yield from node_text_to_md(child_node.content)  # type: ignore


def match_node_tag_name(child_node, used_lang):
    match child_node.tag_name:
        case "att":
            yield from att_to_md(child_node.content)
        case "gi":
            yield from gi_to_md(child_node.content, used_lang)
        case "list":
            yield from list_to_md(child_node.content)
        case "p":
            yield from p_to_md(child_node.content, used_lang)
        case "ref":
            yield from ref_to_md(child_node.content, used_lang)
        case "remarks":
            yield from remarks_to_md(child_node.content, used_lang)
        case "tag":
            yield from tag_to_md(child_node.content)
        case "val":
            yield from val_to_md(child_node.content)
        case _:
            yield from any_to_md(child_node.content)


def convert_node_to_iterable(node: ET.Element) -> Iterator[Node]:
    """Creates an iterator over the content of a ElementTree.

    Args:
        node (ET.Element): The node to convert.

    Yields:
        Iterable[str | ET.Element]: The content of the node.
    """
    if node_has_text_or_tail(node):
        yield Node(getattr(node, "text"), "text")

    if node_has_children(node):
        for child in node:
            yield Node(
                content=child, type="tag", tag_name=split_tag_and_ns(child.tag)[1]
            )

    if node_has_text_or_tail(node, "tail"):
        yield Node(getattr(node, "tail"), "tail")


def att_to_md(node: ET.Element) -> Iterator[str]:
    """Convert an att tag to a markdown representation.

    Args:
        node (Node): The node to convert.

    Raises:
        NodeTransformationError: If the node can't be transformed.

    Yields:
        Iterator[str]: The markdown representation of the node.
    """

    if not node_has_text_or_tail(node):
        raise NodeTransformationError("Can't transform <att/>-tag without content.")

    attr_name, tail = node.text, node.tail

    yield RE_WHITESPACE_START_OR_MULTIPLE.sub(
        "", f"[`@{attr_name}`](#{attr_name}){tail or ''}"
    )


def gi_to_md(node: ET.Element, lang: str | None) -> Iterator[str]:
    """Convert a gi tag to a markdown representation.

    Args:
        node (ET.Element): The node to convert.
        lang: The language of the node.

    Raises:
        NodeTransformationError: If the node can't be transformed.

    Yields:
        str: The markdown representation of the node.
    """
    if not node_has_text_or_tail(node):
        raise NodeTransformationError("Can't transform <gi/>-tag without content.")

    element_name, tail = node.text, node.tail

    yield RE_WHITESPACE_START_OR_MULTIPLE.sub(
        "",
        f"[`<{element_name}>`]({element_name}{f'.{lang}' if lang else ''}.md){tail or ''}",
    )


def list_to_md(node: ET.Element) -> Iterator[str]:
    """Convert a list tag to a markdown representation.

    Args:
        node (ET.Element): The list node to convert.

    Raises:
        NodeTransformationError: If the node can't be transformed.

    Yields:
        str: The markdown representation of the node.
    """

    if not node_has_children(node):
        raise NodeTransformationError("Can't transform <list/>-tag without children.")

    yield (
        "\n\n"
        + "\n".join(["- " + " ".join(transform_node_to_text(item)) for item in node])
        + "\n\n"
        + RE_WHITESPACE_START_OR_MULTIPLE.sub("", node.tail or "")
    )


def p_to_md(node: ET.Element, lang: str | None) -> Iterator[str]:
    """Convert a p tag to a markdown representation.

    Args:
        node (ET.Element): The p node to convert.
        lang: The language of the node.

    Raises:
        NodeTransformationError: If the node can't be transformed.

    Yields:
        str: The markdown representation of the node.
    """

    if not node_has_text_or_tail(node) and not node_has_children(node):
        raise NodeTransformationError("Can't transform <p/>-tag without content.")

    yield "\n\n"

    yield from transform_node_to_text(node, lang)


def ref_to_md(node: ET.Element, lang: str | None) -> Iterator[str]:
    """Convert a ref tag to a markdown representation.

    Args:
        node (ET.Element): The ref node to convert.
        lang: The language of the node.

    Raises:
        NodeTransformationError: If the ref has no target.

    Yields:
        str: The markdown representation of the node.
    """

    target = node.get("target")

    if target is None:
        raise NodeTransformationError("Can't transform <ref/>-tag without a target.")

    processed_target = process_target_attribute(target, lang)

    ref_text, tail = node.text, node.tail

    yield RE_WHITESPACE_START_OR_MULTIPLE.sub(
        "",
        f"[{ref_text}]({processed_target}){tail or ''}",
    )


def remarks_to_md(node: ET.Element, lang: str | None) -> Iterator[str]:
    yield from transform_node_to_text(node, lang)


def tag_to_md(node: ET.Element) -> Iterator[str]:
    """
    Convert a tag to a markdown representation.

    Args:
        node (ET.Element): The node to convert.

    Raises:
        NodeTransformationError: If the node can't be transformed.

    Yields:
        str: The markdown representation of the node.
    """

    if not node_has_text_or_tail(node):
        raise NodeTransformationError("Can't transform <tag/>-tag without content.")

    tag_name, tail = node.text, node.tail

    yield RE_WHITESPACE_START_OR_MULTIPLE.sub(
        "",
        f"`<{tag_name}/>`{tail or ''}",
    )


def val_to_md(node: ET.Element) -> Iterator[str]:
    """
    Convert a val to a markdown representation.

    Args:
        node (ET.Element): The val tag to convert.

    Raises:
        NodeTransformationError: If the node can't be transformed.

    Yields:
        str: The markdown representation of the node.
    """
    if not node_has_text_or_tail(node):
        raise NodeTransformationError("Can't transform <val/>-tag without content.")

    yield RE_WHITESPACE_START_OR_MULTIPLE.sub(
        "",
        f"`{node.text}`{node.tail or ''}",
    )


def any_to_md(node: ET.Element) -> Iterator[str]:
    """Fallback rendering template for unknown tags.

    Args:
        node (ET.Element): The node to convert.

    Raises:
        NodeTransformationError: If the node can't be transformed.

    Yields:
        str: The markdown representation of the node.
    """
    if not node_has_text_or_tail(node) and not node_has_text_or_tail(node, "tail"):
        raise NodeTransformationError(
            f"Can't transform empty {split_tag_and_ns(node.tag)[1]}-tag without text and tail."
        )

    yield RE_WHITESPACE_START_OR_MULTIPLE.sub("", f"{node.text or ''}{node.tail or ''}")


def node_text_to_md(text: str | None) -> Iterator[str]:
    """Convert a node text to a markdown representation.

    Args:
        text (str | None): The text to convert.

    Yields:
        str: The markdown representation of the node.
    """
    if text is None:
        return

    normalized_text = RE_WHITESPACE_START_OR_MULTIPLE.sub("", text)

    if len(normalized_text) == 0:
        return

    yield normalized_text


def node_has_text_or_tail(
    node: ET.Element, part: Literal["text", "tail"] = "text"
) -> bool:
    return bool(getattr(node, part))


def node_has_children(node: ET.Element) -> bool:
    return len(node) > 0


def process_target_attribute(
    target: str, lang: str | None, target_langs: list[str] = DOCS_LANG
) -> str:
    parsed_target = parse.urlparse(target)

    if is_not_link_to_md_file(parsed_target) or lang is None:
        return target

    splitted_path = parsed_target.path.split(".")
    lang_suffix = splitted_path[-2]

    if lang_suffix in target_langs:
        return target

    splitted_path.insert(len(splitted_path) - 1, lang)
    return f"{'.'.join(splitted_path)}{f'#{parsed_target.fragment}' if len(parsed_target.fragment) > 0 else ''}"


def is_not_link_to_md_file(link: parse.ParseResult) -> bool:
    if not link.path.endswith(".md"):
        return True
    if len(link.scheme) > 0:
        return True
    return False

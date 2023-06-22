def split_tag_and_ns(tag: str) -> tuple[str, str]:
    """Split a tag into its namespace and its tag name.

    Args:
        tag (str): The tag to split.

    Returns:
        tuple[str, str]: The namespace and the tag name.
    """
    if "}" not in tag:
        return "", tag

    ns, tag_name = tag[1:].split("}")

    return ns, tag_name

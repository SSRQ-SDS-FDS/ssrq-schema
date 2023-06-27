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


def translate_datatype(datatype: str, translations: dict[str, str]) -> str:
    match datatype:
        case "ID":
            return translations["id"]
        case "IDREF" | "IDREFS":
            return translations["idRef"]
        case "string" | "token":
            return translations["string"]
        case "positiveInteger" | "int":
            return translations["int"]
        case "double" | "float" | "decimal":
            return translations["float"]
        case _:
            return datatype

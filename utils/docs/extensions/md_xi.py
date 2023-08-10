import re
from dataclasses import dataclass

XI_PATTERN = re.compile(
    r"-+xi-include-+\s([A-Za-z0-9_\-]+\.[a-z]+)(?:#([A-Za-z0-9_\-]+))?"
)


@dataclass(frozen=True)
class XInclude:
    filename: str
    xpointer: str | None


def find_xi_includes(
    text: str, pattern: re.Pattern = XI_PATTERN
) -> list[XInclude] | None:
    """A simple parsing function to find `-xi-include- <filename>#<xpointer>` directives
    in a string. This function is supposed to be used as a Markdown extension.

    Args:
        text (str): The text to parse.
        pattern (re.Pattern): The pattern to use for parsing. Defaults to XI_PATTERN.

    Returns:
        list[XInclude] | None: A list of XInclude objects or None if no XInclude was found.
    """
    results = re.findall(pattern, text)

    if len(results) == 0:
        return None

    return [
        XInclude(filename=result[0], xpointer=result[1] if len(result[1]) > 0 else None)
        for result in results
    ]

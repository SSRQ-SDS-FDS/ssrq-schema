import re
from dataclasses import dataclass
from pathlib import Path

from saxonche import (
    PySaxonProcessor,
    PyXdmNode,
    PyXPathProcessor,
    PyXslt30Processor,
    PyXsltExecutable,
)

import utils.commons.config as configs

XI_PATTERN = re.compile(
    r"-+xi-include-+\s([A-Za-z0-9_\-]+\.[a-z]+)(?:#([A-Za-z0-9_\-]+))?"
)


@dataclass(frozen=True)
class XInclude:
    filename: str
    xpointer: str | None


@dataclass(frozen=True)
class ResolvedXInclude:
    include: XInclude
    content: str


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


def resolve_xi_includes(
    includes: list[XInclude], base_path: Path = configs.EXAMPLES_DIR.absolute()
) -> list[ResolvedXInclude]:
    resolved_includes: list[ResolvedXInclude] = []

    with PySaxonProcessor(license=False) as proc:
        xslt_proc: PyXslt30Processor = proc.new_xslt30_processor()

        for include in includes:
            document: PyXdmNode = find_element_by_xi_pointer(
                saxon_proc=proc,
                node=proc.parse_xml(xml_file_name=str(base_path / include.filename)),
                include=include,
            )

            xslt_proc.set_parameter(  # type: ignore
                "path_base", proc.make_string_value(base_path.as_uri())  # type: ignore
            )

            xsl: PyXsltExecutable = xslt_proc.compile_stylesheet(  # type: ignore
                stylesheet_file=str(configs.XSLTS["xi"])
            )
            xslt_result: str = xsl.transform_to_string(xdm_node=document)

            if xslt_result is None:
                raise ValueError(f"Failed to resolve xincludes for {include.filename}")

            resolved_includes.append(
                ResolvedXInclude(include=include, content=xslt_result)
            )

    return resolved_includes


def find_element_by_xi_pointer(
    saxon_proc: PySaxonProcessor, node: PyXdmNode, include: XInclude
) -> PyXdmNode:
    if include.xpointer is None:
        return node

    xpath_proc: PyXPathProcessor = saxon_proc.new_xpath_processor()
    xpath_proc.set_context(xdm_item=node)

    if (
        xi_query := xpath_proc.evaluate_single(f"//*[@xml:id = '{include.xpointer}']")
    ) is not None:
        return xi_query.get_node_value()

    raise ValueError(f"Could not find the id {include.xpointer} in {include.filename}")

import re
from collections import defaultdict
from pathlib import PurePath

from mkdocs.structure.files import File, Files
from mkdocs.structure.files import utils as mkdocs_file_utils

from utils.commons import config as configs
from utils.commons.logger import LOGGER

RE_MD_LINKS = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def replace_with_relative_links(markdown: str, context: File, files: Files) -> str:
    """Replace all links to files with relative links.
    This plugin can be used in the `on_page_markdown` hook.

    Args:
        markdown (str): The markdown content of the page.
        context (File): The file that links to other files.
        files (Files): The files that are linked to.

    Returns:
            str: The markdown content with relative links
                 or the original markdown if there are no links to replace."""

    extracted_links = extract_links_from_md(markdown)

    if extracted_links is None:
        return markdown

    filtered_links = filter_markdown_links(extracted_links)

    if filtered_links is None:
        return markdown

    file_lookup_table = init_file_lookup_table(files)

    for link in filtered_links:
        if (target_file := find_file_by_name(files, link, file_lookup_table)) is None:
            continue

        relative_link = create_relative_link(linker=context, target=target_file)

        markdown = re.sub(
            pattern=rf"\({link}(#.*)?\)", repl=f"({relative_link}\\1)", string=markdown
        )

    return markdown


def extract_links_from_md(
    markdown: str, pattern: re.Pattern = RE_MD_LINKS
) -> list[str] | None:
    matched_links: list[str] = RE_MD_LINKS.findall(markdown, re.MULTILINE)

    if len(matched_links) == 0:
        return None

    return matched_links


def filter_markdown_links(links: list[str]) -> set[str] | None:
    from urllib.parse import urlparse

    filtered_links: set[str] = {
        parsed_url.path
        for link in links
        if (parsed_url := urlparse(link)).scheme == ""
        and parsed_url.path.endswith(configs.SUPPORTED_FILE_TYPES)
    }

    if len(filtered_links) == 0:
        return None

    return filtered_links


def init_file_lookup_table(files: Files) -> dict[str, list[File]]:
    file_list: dict[str, list[File]] = defaultdict(list)

    for file in files:
        filename = PurePath(file.abs_src_path).name  # type: ignore
        file_list[filename].append(file)

    return file_list


def find_file_by_name(
    files: Files, filename: str, file_lookup_table: dict[str, list[File]]
) -> File | None:
    if (matched_files := file_lookup_table.get(filename)) is None:
        return None

    if len(matched_files) > 1:
        LOGGER.warning(
            f"Found multiple files with the name {filename}. "
            f"Using the first one: {matched_files[0].abs_src_path}"
        )

    return matched_files[0]


def create_relative_link(linker: File, target: File) -> str:
    """Create a relative link from a linker file to a target file.

    Args:
        linker (File): The file that links to the target file.
        target (File): The file that is linked to.

    Returns:
        str: The relative link."""

    return mkdocs_file_utils.get_relative_url(target.abs_src_path, linker.abs_src_path)  # type: ignore

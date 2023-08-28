from pathlib import PurePath

import pytest
from mkdocs.structure.files import File, Files

from utils.docs.extensions import magic_links


@pytest.fixture(scope="module")
def files() -> Files:
    return Files(
        [
            File(
                path=str(path),
                src_dir=str(path.parent),
                dest_dir=".",
                use_directory_urls=False,
            )
            for path in [
                PurePath("/docs/one/foo.md"),
                PurePath("/docs/two/foo.md"),
                PurePath("/docs/three/bar.md"),
            ]
        ]
    )


@pytest.fixture(scope="module")
def markdown() -> str:
    return """
    # Title

    This is a [link_a](https://linka.com) to a website.

    This is a [link_b](https://linkb.com) to a website with a [link_c](https://linkc.com) inside.

    This is a [link_d](foo.md) to a file with a [link_e](https://link_e.com)
    inside and a [link_f](https://link_f.com) at the end.

    """


def test_replace_with_relative_links(files: Files, markdown: str):
    linker = list(files)[2]

    replacement_result = magic_links.replace_with_relative_links(
        markdown, linker, files
    )

    links_from_replace = magic_links.extract_links_from_md(replacement_result)

    assert links_from_replace is not None

    filtered_links = magic_links.filter_markdown_links(links_from_replace)

    assert filtered_links is not None

    assert len(filtered_links) == 1

    assert filtered_links[0] == "../one/foo.md"


def test_filter_markdown_links():
    links = [
        "https://linka.com",
        "https://linkb.com",
        "https://linkc.com",
        "foo.md",
        "https://link_e.com",
        "https://link_f.com",
    ]

    assert magic_links.filter_markdown_links(links) == [
        "foo.md",
    ]

    links.pop(3)

    assert magic_links.filter_markdown_links(links) is None


def test_extract_links_from_md(markdown: str):
    assert magic_links.extract_links_from_md(markdown) == [
        "https://linka.com",
        "https://linkb.com",
        "https://linkc.com",
        "foo.md",
        "https://link_e.com",
        "https://link_f.com",
    ]


def test_init_file_lookup_table(files: Files):
    file_lookup_table = magic_links.init_file_lookup_table(files)

    assert list(file_lookup_table.keys()) == ["foo.md", "bar.md"]
    assert len(file_lookup_table["foo.md"]) == 2


def test_find_file_by_name(files: Files, caplog):
    lookup_table = magic_links.init_file_lookup_table(files)

    result_foo = magic_links.find_file_by_name(
        files=files, filename="foo.md", file_lookup_table=lookup_table
    )

    result_bar = magic_links.find_file_by_name(
        files=files, filename="bar.md", file_lookup_table=lookup_table
    )

    result_unknown = magic_links.find_file_by_name(
        files=files, filename="unknown.md", file_lookup_table=lookup_table
    )

    assert result_foo is not None
    for record in caplog.records:
        assert record.levelname == "WARNING"
        assert "Found multiple files with the name foo.md" in record.message
    assert isinstance(result_foo, File)

    assert result_bar is not None
    assert isinstance(result_bar, File)

    assert result_unknown is None


def test_create_relative_link(files: Files):
    linker = list(files)[0]
    target = list(files)[1]

    assert (
        magic_links.create_relative_link(linker=linker, target=target)
        == "../two/foo.md"
    )

    asset = PurePath("/docs/assets/css/foo.css")

    target = File(
        path=str(asset),
        src_dir=str(asset.parent),
        dest_dir=".",
        use_directory_urls=False,
    )

    assert (
        magic_links.create_relative_link(linker=linker, target=target)
        == "../assets/css/foo.css"
    )

import pytest

from utils.docs.extensions.md_xi import XInclude, find_xi_includes


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", None),
        ("xi-include- bar.xml#foo", None),
        (
            "foo -xi-include- bar.xml",
            [XInclude(filename="bar.xml", xpointer=None)],
        ),
        (
            """Bar -xi-include- foo.xml#bar
            -xi-include- bar.xml#foo bar bar bar
            foo foo --xi-include- bar_3.xml
            -xi-include-bar_4.xml foo foo""",
            [
                XInclude(filename="foo.xml", xpointer="bar"),
                XInclude(filename="bar.xml", xpointer="foo"),
                XInclude(filename="bar_3.xml", xpointer=None),
            ],
        ),
    ],
)
def test_find_xi_includes(text: str, expected: list[XInclude] | None):
    assert find_xi_includes(text) == expected

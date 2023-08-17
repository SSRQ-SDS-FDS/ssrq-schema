from pathlib import Path

import pytest
from saxonche import (
    PySaxonProcessor,
)

from utils.docs.extensions.md_xi import (
    ResolvedXInclude,
    XInclude,
    find_element_by_xi_pointer,
    find_xi_includes,
    resolve_xi_includes,
)


@pytest.fixture(scope="function")
def tmp_path_with_ex(tmp_path: Path) -> Path:
    with open(tmp_path / "xi_ex.xml", "w") as ex:
        ex.write("<seg xmlns='http://www.tei-c.org/ns/Examples'>world</seg>")
    return tmp_path


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


@pytest.mark.parametrize(
    "xml, xi, expected",
    [
        ("<foo/>", XInclude(filename="bar.xml", xpointer=None), "<foo/>"),
        (
            """<div xmlns="http://www.tei-c.org/ns/1.0"><egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ex-origDate-abbr">
            <origDate when-custom="--11-10" calendar="gregorian">10. <abbr>9bris</abbr></origDate>
            </egXML></div>""",
            XInclude(filename="bar.xml", xpointer="ex-origDate-abbr"),
            """<egXML xmlns="http://www.tei-c.org/ns/Examples">
            <origDate when-custom="--11-10" calendar="gregorian">10. <abbr>9bris</abbr>
            </origDate></egXML>""",
        ),
        (
            """<div xmlns="http://www.tei-c.org/ns/1.0" xmlns:xi="http://www.w3.org/2001/XInclude"><egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ex-origDate-abbr">
            <origDate when-custom="--11-10" calendar="gregorian">10. <abbr>9bris</abbr></origDate>
            <xi:include href="xi_ex.xml"/>
            </egXML></div>""",
            XInclude(filename="bar.xml", xpointer="ex-origDate-abbr"),
            """<egXML xmlns="http://www.tei-c.org/ns/Examples">
            <origDate  when-custom="--11-10" calendar="gregorian">10. <abbr>9bris</abbr>
            </origDate><seg>world</seg></egXML>""",
        ),
    ],
)
def test_resolve_xi_includes(
    tmp_path_with_ex: Path, xml: str, xi: XInclude, expected: str
):
    with open(tmp_path_with_ex / xi.filename, "w") as ex:
        ex.write(xml)

    results = list(
        map(
            lambda r: ResolvedXInclude(
                include=r.include,
                content=r.content.replace(
                    'xmlns:xi="http://www.w3.org/2001/XInclude"',
                    "",  # removing xi-namespaces, because they are irrelevant for testing
                ),
            ),
            resolve_xi_includes(base_path=tmp_path_with_ex, includes=[xi]),
        )
    )

    assert len(results) == 1

    with PySaxonProcessor(license=False) as proc:
        assert (
            proc.parse_xml(xml_text=results[0].content).__str__()
            == proc.parse_xml(xml_text=expected).__str__()
        )


@pytest.mark.parametrize(
    "xml, xi, expected",
    [
        ("<foo/>", XInclude(filename="bar.xml", xpointer=None), "<foo/>"),
        (
            """<div xmlns="http://www.tei-c.org/ns/1.0"><egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ex-origDate-abbr">
            <origDate when-custom="--11-10" calendar="gregorian">10. <abbr>9bris</abbr></origDate>
            </egXML></div>""",
            XInclude(filename="bar.xml", xpointer="ex-origDate-abbr"),
            """<egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ex-origDate-abbr">
            <origDate when-custom="--11-10" calendar="gregorian">10. <abbr>9bris</abbr>
            </origDate></egXML>""",
        ),
    ],
)
def test_find_element_by_xi_pointer(xml: str, xi: XInclude, expected: str):
    with PySaxonProcessor(license=False) as proc:
        node = proc.parse_xml(xml_text=xml)
        assert (
            find_element_by_xi_pointer(saxon_proc=proc, node=node, include=xi).__str__()
            == proc.parse_xml(
                xml_text=expected
            ).__str__()  # testing the equality of the string representation, not the objects itself (which are never equal)
        )


@pytest.mark.parametrize(
    "xml, xi",
    [
        ("<foo/>", XInclude(filename="bar.xml", xpointer="bar")),
        (
            """<div xmlns="http://www.tei-c.org/ns/1.0"><egXML xmlns="http://www.tei-c.org/ns/Examples" xml:id="ex-origDate-abbr">
            <origDate when-custom="--11-10" calendar="gregorian">10. <abbr>9bris</abbr></origDate>
            </egXML></div>""",
            XInclude(filename="bar.xml", xpointer="xyz"),
        ),
    ],
)
def test_find_element_by_xi_pointer_raises_error_for_unknown_id(
    xml: str,
    xi: XInclude,
):
    with pytest.raises(ValueError):
        with PySaxonProcessor(license=False) as proc:
            node = proc.parse_xml(xml_text=xml)
            find_element_by_xi_pointer(saxon_proc=proc, node=node, include=xi)

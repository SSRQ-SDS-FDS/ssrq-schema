import xml.etree.ElementTree as ET

import pytest

from utils.docs.helpers import node_to_text


@pytest.mark.parametrize(
    "node, expected",
    [
        (
            ET.fromstring(
                "<desc xml:lang='de'>Enthält die einfache Hervorhebung mit <gi>hi</gi>-Elementen.</desc>"
            ),
            "Enthält die einfache Hervorhebung mit [`<hi>`](hi.de.md)-Elementen.",
        ),
        (
            ET.fromstring(
                """
<desc xml:lang="de" versionDate="2023-05-16">Erfassung Zeitspanne
                nach <ref target="https://de.wikipedia.org/wiki/ISO_8601#Zeitspannen">ISO 8601</ref>.
                Beginnt mit dem Kürzel P (Periode) gefolgt T (Time) und arabischen Ziffern. Sich
                wiederholende Zeitspannenden werden im vollen Format ausgedrückt und beginnen mit
                dem Kürzel R (Repeated). Ansonsten werden folgende Werte vergeben
                <list><item>H = hour</item><item>M = minute</item><item>S = second</item></list>
            </desc>
            """
            ),
            "Erfassung Zeitspanne nach [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601#Zeitspannen). Beginnt mit dem Kürzel P (Periode) gefolgt T (Time) und arabischen Ziffern. Sich wiederholende Zeitspannenden werden im vollen Format ausgedrückt und beginnen mit dem Kürzel R (Repeated). Ansonsten werden folgende Werte vergeben \n\n- H = hour\n- M = minute\n- S = second\n\n",
        ),
        (
            ET.fromstring(
                "<remarks xml:lang='de'>Foo <ref target='baz.md'>bar</ref> foo</remarks>"
            ),
            "Foo [bar](baz.de.md) foo",
        ),
        (
            ET.fromstring(
                """<remarks xml:lang='de'><p>Foo <ref target='baz_one.md'>bar one</ref> foo</p>
                    <p>Foo <ref target='baz_two.md'>bar two</ref> foo</p>
                </remarks>
                """
            ),
            "\n\n Foo [bar one](baz_one.de.md) foo \n\n Foo [bar two](baz_two.de.md) foo",
        ),
    ],
)
def test_node_to_text_representation_end2end(node: ET.Element, expected: str):
    """Test if the node is converted correctly."""

    result = node_to_text.transform_node_to_text(node)

    assert " ".join(result) == expected


def test_any_to_md():
    node = ET.Element("any")
    node.text = "foo"
    assert list(node_to_text.any_to_md(node)) == ["foo"]

    node.tail = " bar"
    assert list(node_to_text.any_to_md(node)) == ["foo bar"]


@pytest.mark.parametrize(
    "node, expected",
    [
        (
            ET.fromstring("<att>foo</att>"),
            "[`@foo`](#foo)",
        ),
        (
            ET.fromstring("<bar><att>foo</att>-faz</bar>")[0],
            "[`@foo`](#foo)-faz",
        ),
        (
            ET.fromstring("<bar><att>foo</att> faz</bar>")[0],
            "[`@foo`](#foo) faz",
        ),
    ],
)
def test_att_to_md(node: ET.Element, expected: str):
    """Test if the att tag is converted correctly."""

    result = list(node_to_text.att_to_md(node))

    assert len(result) == 1
    assert result[0] == expected


@pytest.mark.parametrize(
    "node, lang, expected",
    [
        (
            ET.fromstring("<gi>foo</gi>"),
            None,
            "[`<foo>`](foo.md)",
        ),
        (
            ET.fromstring("<gi>foo</gi>"),
            "de",
            "[`<foo>`](foo.de.md)",
        ),
        (
            ET.fromstring("<spec><gi>hi</gi>-Element</spec>")[0],
            "de",
            "[`<hi>`](hi.de.md)-Element",
        ),
    ],
)
def test_gi_to_md(node: ET.Element, lang: str | None, expected: str):
    """Test if the gi tag is converted correctly."""

    result = list(node_to_text.gi_to_md(node, lang))

    assert len(result) == 1
    assert result[0] == expected


@pytest.mark.parametrize(
    "node, expected",
    [
        (
            ET.fromstring("<list><item>foo</item><item>bar</item></list>"),
            "\n\n- foo\n- bar\n\n",
        ),
        (
            ET.fromstring("<list><item>faz <gi>foo</gi></item><item>bar</item></list>"),
            "\n\n- faz [`<foo>`](foo.md)\n- bar\n\n",
        ),
    ],
)
def test_list_to_md(node: ET.Element, expected: str):
    """Test if the list tag is converted correctly."""

    result = list(node_to_text.list_to_md(node))

    assert len(result) == 1
    assert result[0] == expected


def test_empty_list_raises_error():
    node = ET.fromstring("<list></list>")
    with pytest.raises(node_to_text.NodeTransformationError):
        list(node_to_text.list_to_md(node))


def test_p_to_md():
    node = ET.Element("p")
    node.text = "foo"
    assert " ".join(node_to_text.p_to_md(node, None)) == "\n\n foo"

    node.tail = " bar"
    assert " ".join(node_to_text.p_to_md(node, None)) == "\n\n foo bar"


@pytest.mark.parametrize(
    "node, expected",
    [
        (
            ET.fromstring("<ref target='bar.md'>foo</ref>"),
            "[foo](bar.md)",
        ),
        (
            ET.fromstring("<desc><ref target='bar.de.md'>foo</ref> baz</desc>")[0],
            "[foo](bar.de.md) baz",
        ),
    ],
)
def test_ref_to_md(node: ET.Element, expected: str):
    """Test if the ref tag is converted correctly."""

    result = list(node_to_text.ref_to_md(node, None))

    assert len(result) == 1
    assert result[0] == expected


@pytest.mark.parametrize(
    "node, expected",
    [
        (ET.fromstring("<remarks>foo</remarks>"), "foo"),
    ],
)
def test_remarks_to_md(node: ET.Element, expected: str):
    """Test if the remarks tag is converted correctly."""

    result = " ".join(node_to_text.remarks_to_md(node, None))

    assert result == expected


def test_tag_to_md():
    node = ET.Element("tag")
    node.text = "gap reason='missing'"
    assert list(node_to_text.tag_to_md(node)) == ["`<gap reason='missing'/>`"]

    node.tail = " bar"
    assert list(node_to_text.tag_to_md(node)) == ["`<gap reason='missing'/>` bar"]


def test_val_to_md():
    node = ET.Element("val")
    node.text = "foo"
    assert list(node_to_text.val_to_md(node)) == ["`foo`"]

    node.tail = " bar"
    assert list(node_to_text.val_to_md(node)) == ["`foo` bar"]


def test_convert_node_to_iterable():
    node = ET.Element("node")
    assert list(node_to_text.convert_node_to_iterable(node)) == []

    node.text = "foo"
    assert list(node_to_text.convert_node_to_iterable(node)) == [
        node_to_text.Node("foo", "text")
    ]

    node.append(ET.Element("child_one"))
    node.append(ET.Element("child_two"))
    assert list(node_to_text.convert_node_to_iterable(node)) == [
        node_to_text.Node("foo", "text"),
        node_to_text.Node(node[0], "tag", "child_one"),
        node_to_text.Node(node[1], "tag", "child_two"),
    ]

    node.tail = "bar"
    assert list(node_to_text.convert_node_to_iterable(node)) == [
        node_to_text.Node("foo", "text"),
        node_to_text.Node(node[0], "tag", "child_one"),
        node_to_text.Node(node[1], "tag", "child_two"),
        node_to_text.Node("bar", "tail"),
    ]


@pytest.mark.parametrize(
    "target, lang, expected",
    [
        ("foo.md", None, "foo.md"),
        ("foo.md", "de", "foo.de.md"),
        ("foo.de.md", "fr", "foo.de.md"),
        ("foo", "de", "foo"),
        ("foo.md#bar", "de", "foo.de.md#bar"),
        (
            "hand.md#8-behandlung-redaktioneller-eingriffe-des-schreibers",
            "de",
            "hand.de.md#8-behandlung-redaktioneller-eingriffe-des-schreibers",
        ),
    ],
)
def test_process_target_attribute(target: str, lang: str | None, expected: str):
    assert node_to_text.process_target_attribute(target, lang) == expected


def test_node_has_text():
    node = ET.Element("node")
    assert node_to_text.node_has_text_or_tail(node) is False

    node.text = "text"
    assert node_to_text.node_has_text_or_tail(node) is True


def test_node_has_children():
    node = ET.Element("node")
    assert node_to_text.node_has_children(node) is False

    node.append(ET.Element("child"))
    assert node_to_text.node_has_children(node) is True

from test.conftest import RNG_test_function

import pytest


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-titleStmt",
            """<titleStmt>
                <title>I. Abteilung: Die Rechtsquellen des Kantons Zürich. Neue Folge. Zweiter Teil:
                    Rechte der Landschaft. Band 11: Die Obervogteien um die Stadt Zürich</title>
                <editor>
                    <persName>Ariane Huber Hernández</persName>
                </editor>
                <editor>
                    <persName>Michael Nadig</persName>
                </editor>
                <respStmt>
                    <persName>Ariane Huber Hernández</persName>
                    <persName>Michael Nadig</persName>
                    <resp>Transkription</resp>
                </respStmt>
                <respStmt>
                    <persName>Ariane Huber Hernández</persName>
                    <persName>Michael Nadig</persName>
                    <resp>XML-Codierung des Transkripts</resp>
                </respStmt>
            </titleStmt>""",
            True,
        ),
        (
            "invalid-titleStmt-without-editor",
            """<titleStmt>
                <title>I. Abteilung: Die Rechtsquellen des Kantons Zürich. Neue Folge. Zweiter Teil:
                    Rechte der Landschaft. Band 11: Die Obervogteien um die Stadt Zürich</title>
                <respStmt>
                    <persName>Ariane Huber Hernández</persName>
                    <persName>Michael Nadig</persName>
                    <resp>Transkription</resp>
                </respStmt>
                <respStmt>
                    <persName>Ariane Huber Hernández</persName>
                    <persName>Michael Nadig</persName>
                    <resp>XML-Codierung des Transkripts</resp>
                </respStmt>
            </titleStmt>""",
            False,
        ),
        (
            "invalid-titleStmt-with-attribute",
            """<titleStmt xml:id='bar'>
                <title>I. Abteilung: Die Rechtsquellen des Kantons Zürich. Neue Folge. Zweiter Teil:
                    Rechte der Landschaft. Band 11: Die Obervogteien um die Stadt Zürich</title>
                <editor>
                    <persName>Ariane Huber Hernández</persName>
                </editor>
                <editor>
                    <persName>Michael Nadig</persName>
                </editor>
                <respStmt>
                    <persName>Ariane Huber Hernández</persName>
                    <persName>Michael Nadig</persName>
                    <resp>Transkription</resp>
                </respStmt>
                <respStmt>
                    <persName>Ariane Huber Hernández</persName>
                    <persName>Michael Nadig</persName>
                    <resp>XML-Codierung des Transkripts</resp>
                </respStmt>
            </titleStmt>""",
            False,
        ),
    ],
)
def test_titleStmt_rng(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("titleStmt", name, markup, result, False)

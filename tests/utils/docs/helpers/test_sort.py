import pytest

from utils.docs.helpers.sort import sort_with_uca


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            ["Apfel", "Appelbaum", "Äpfel", "appel"],
            [
                "Apfel",
                "Äpfel",
                "appel",
                "Appelbaum",
            ],
        ),
        (
            ["del", "add", "addSpan", "TEI", "msDesc"],
            [
                "add",
                "addSpan",
                "del",
                "msDesc",
                "TEI",
            ],
        ),
    ],
)
def test_sort_with_strings(inputs: list[str], expected: list[str]):
    assert sort_with_uca(inputs) == expected


def test_sort_with_class():
    from dataclasses import dataclass

    @dataclass
    class Dummy:
        name: str

    inputs = [
        Dummy("Apfel"),
        Dummy("Appelbaum"),
        Dummy("Äpfel"),
    ]

    expected = [
        Dummy("Apfel"),
        Dummy("Äpfel"),
        Dummy("Appelbaum"),
    ]

    assert sort_with_uca(inputs, lambda i: i.name) == expected

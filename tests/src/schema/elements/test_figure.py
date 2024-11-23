import pytest
from pyschval.schematron.validate import apply_schematron_validation
from pyschval.types.result import SchematronResult

from ..conftest import RNG_test_function, SimpleTEIWriter, add_tei_namespace


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-figure-without-content",
            "<figure type='locus_sigilli'/>",
            True,
        ),
        (
            "valid-figure-with-graphic",
            """
            <figure type='illustration'>
                <graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/>
            </figure>
            """,
            True,
        ),
        (
            "valid-figure-with-graphic-and-head",
            """
            <figure type='illustration'>
                <graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/>
                <head>Foo</head>
            </figure>
            """,
            True,
        ),
        (
            "valid-figure-with-hand",
            "<figure type='copper_engraving' hand='otherHand'/>",
            True,
        ),
        (
            "valid-figure-with-place",
            "<figure type='copper_engraving' place='above'/>",
            True,
        ),
    ],
)
def test_figure(
    test_element_with_rng: RNG_test_function,
    name: str,
    markup: str,
    result: bool,
):
    test_element_with_rng("figure", name, markup, result, False)


@pytest.mark.parametrize(
    "name, markup, result",
    [
        (
            "valid-figure-with-type-illustration",
            """
            <figure type='illustration'>
                <graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/>
            </figure>
            """,
            True,
        ),
        (
            "invalid-figure-with-type-illustration-but-without-graphic",
            "<figure type='illustration'/>",
            False,
        ),
        (
            "valid-figure-with-other-type",
            "<figure type='locus_sigilli'/>",
            True,
        ),
        (
            "invalid-figure-with-other-type",
            """
            <figure type='locus_sigilli'>
                <graphic type='familytree' mimeType='image/jpg' url='foo.jpg'/>
            </figure>
            """,
            False,
        ),
    ],
)
def test_figure_constraints(
    main_constraints: str, writer: SimpleTEIWriter, name: str, markup: str, result: bool
):
    writer.write(name, add_tei_namespace(markup))
    reports: list[SchematronResult] = apply_schematron_validation(
        input=writer.list(), isosch=main_constraints
    )
    assert reports[0].report.is_valid() is result

from pyschval.schematron.create import create_schematron_stylesheet


def test_schematron_compilation(
    main_constraints: str,
):
    """Test if the schematron file can be compiled."""

    compiled_schema = create_schematron_stylesheet(main_constraints)

    assert isinstance(compiled_schema, str) is True

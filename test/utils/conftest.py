from typing import Optional

import pytest
from saxonche import PySaxonProcessor, PyXdmItem


def check_result_with_xpath(
    xml: str, xpath: str, expected_result: Optional[bool]
) -> Optional[PyXdmItem]:
    with PySaxonProcessor(license=False) as proc:
        xml_node = proc.parse_xml(xml_text=xml)
        xp = proc.new_xpath_processor()
        xp.declare_namespace(prefix="tei", uri="http://www.tei-c.org/ns/1.0")
        xp.set_context(xdm_item=xml_node)  # type: ignore
        eval_result: bool | Optional[PyXdmItem] = (
            xp.evaluate_single(xpath)
            if expected_result is None
            else xp.effective_boolean_value(xpath)
        )
        if expected_result is None:
            return eval_result
        assert eval_result == expected_result


@pytest.fixture
def example_odd() -> str:
    from pathlib import Path

    with open(
        Path(__file__).parent.parent.absolute() / "examples/odd_example.xml", "r"
    ) as f:
        return f.read()

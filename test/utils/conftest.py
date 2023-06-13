import xml.etree.ElementTree as ET
from typing import Callable, Optional

import pytest
from saxonche import PySaxonProcessor, PyXdmItem

from utils.odd2md import NS_MAP

EL_FINDER = Callable[[str], ET.Element | None]


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


@pytest.fixture(scope="session")
def example_odd() -> str:
    from pathlib import Path

    with open(
        Path(__file__).parent.parent.absolute() / "examples/odd_example.xml", "r"
    ) as f:
        return f.read()


@pytest.fixture(scope="session")
def example_elementSpec(example_odd: str) -> EL_FINDER:
    parsed_odd = ET.fromstring(example_odd)

    def get_element_spec(ident: str) -> ET.Element | None:
        return parsed_odd.find(f".//tei:elementSpec[@ident='{ident}']", NS_MAP)

    return get_element_spec

from dataclasses import dataclass
from typing import Literal

import pytest
from saxonche import PySaxonProcessor, PyXdmAtomicValue, PyXsltExecutable

from utils.main import XSLT_BASE


@dataclass
class XsltParam:
    name: str
    type: Literal["xs:string", "xs:integer"]
    value: list[str] | str


def create_saxon_values(proc: PySaxonProcessor, param: XsltParam) -> PyXdmAtomicValue:
    match param.type:
        case "xs:string":
            return (
                proc.make_string_value(param.value)
                if isinstance(param.value, str)
                else proc.make_array(
                    [proc.make_string_value(value) for value in param.value]
                )
            )
        case "xs:integer":
            return (
                proc.make_integer_value(param.value)
                if isinstance(param.value, str)
                else proc.make_array(
                    [proc.make_integer_value(value) for value in param.value]
                )
            )
        case _:
            raise ValueError(f"Unknown type: {type}")


def apply_xsl(xml: str, xsl_name: str, params: list[XsltParam]) -> str:
    with PySaxonProcessor(license=False) as proc:
        xml_node = proc.parse_xml(xml_text=xml)
        xsl_proc = proc.new_xslt30_processor()
        for param in params:
            xsl_proc.set_parameter(
                name=param.name,
                value=create_saxon_values(proc=proc, param=param),
            )
        xsl: PyXsltExecutable = xsl_proc.compile_stylesheet(
            stylesheet_file=str(XSLT_BASE / xsl_name)
        )

        result: str = xsl.transform_to_string(xdm_node=xml_node)
    return result


def check_result_with_xpath(xml: str, xpath: str, result: bool) -> None:
    with PySaxonProcessor(license=False) as proc:
        xml_node = proc.parse_xml(xml_text=xml)
        xp = proc.new_xpath_processor()
        xp.declare_namespace(prefix="tei", uri="http://www.tei-c.org/ns/1.0")
        xp.set_context(xdm_item=xml_node)  # type: ignore
        eval_result: bool = xp.effective_boolean_value(xpath)
        assert eval_result == result


@pytest.fixture
def example_odd() -> str:
    from pathlib import Path

    with open(
        Path(__file__).parent.parent.absolute() / "examples/odd_example.xml", "r"
    ) as f:
        return f.read()

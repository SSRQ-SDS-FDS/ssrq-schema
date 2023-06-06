from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from saxonche import (
    PySaxonProcessor,
    PyXdmAtomicValue,
    PyXdmMap,
    PyXsltExecutable,
)

from utils.main import XSLT_BASE, Schema, load_config, odd_factory

LANGS = ["de", "fr"]
RESOLVE_XSL = "resolve-internal-references.xsl"
SPEC_TO_MD_XSL = "odd-to-md.xsl"


def create_schema_by_entry(entry_point: str) -> Schema | None:
    """Create a schema from the config file.

    Args:
        entry_point (str): The name of the entry point.

    Returns:
        Schema | None: A schema class instance if it exists, None otherwise.
    """
    config = load_config()

    if config is not None:
        schema_config = [
            schema for schema in config.schemas if schema["entry"] == entry_point
        ][0]
        return odd_factory(
            schema_config=schema_config,
            authors=config.authors,
        )


@dataclass
class XsltParam:
    """A class to represent an XSLT parameter."""

    name: str
    type: Literal["xs:string", "xs:integer"]
    value: list[str] | str


def create_saxon_values(proc: PySaxonProcessor, param: XsltParam) -> PyXdmAtomicValue:
    """Create a Saxon value from a XsltParam.

    Args:
        proc (PySaxonProcessor): The Saxon processor.
        param (XsltParam): The XSLT parameter.

    Returns:
        PyXdmAtomicValue: The Saxon value."""

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


def apply_xsl(xml: str, xsl_name: str, params: list[XsltParam] | None = None) -> str:
    """A helper function to apply an XSLT stylesheet to an XML document.

    Args:
        xml (str): The XML document.
        xsl_name (str): The name of the XSLT stylesheet.
        params (list[XsltParam] | None, optional): The parameters to pass to the stylesheet. Defaults to None.

    Returns:
        str: The result of the transformation."""

    with PySaxonProcessor(license=False) as proc:
        xml_node = proc.parse_xml(xml_text=xml)
        xsl_proc = proc.new_xslt30_processor()

        if params is not None:
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


class ODD2Md:
    """A class which helps to streamline the process of converting ODD files to Markdown."""

    schema: str
    languages: list[str]
    el_spec_name: str = "elementSpec"
    out_dir: Path

    def __init__(
        self, schema: Schema | str, languages: list[str], target_dir: str
    ) -> None:
        """Initialize the class.

        Args:
            schema (Schema): The schema class instance.
            languages (list[str]): The languages to convert.
        """
        self.out_dir = Path(target_dir)
        self.languages = languages
        self.schema = schema.compiled_odd if isinstance(schema, Schema) else schema

    def create_md_doc_per_lang(self) -> None:
        """Create a markdown documentation per element per language.

        Returns:
            None: Nothing."""

        resolved_odd = apply_xsl(
            xml=self.schema,
            xsl_name=RESOLVE_XSL,
        )
        for lang in self.languages:
            odd_to_md = apply_xsl(
                xml=resolved_odd,
                xsl_name=SPEC_TO_MD_XSL,
                params=[
                    XsltParam(
                        name="lang",
                        type="xs:string",
                        value=lang,
                    )
                ],
            )
            self.store_md_doc_per_lang(md_doc=odd_to_md, lang=lang)

    def store_md_doc_per_lang(self, md_doc: str, lang: str) -> None:
        """Store the markdown documentation per element per language.

        Args:
            md_doc (str): The markdown documentation.
            lang (str): The language.

        Returns:
            None: Nothing."""

        with PySaxonProcessor(license=False) as proc:
            docs = proc.parse_xml(xml_text=md_doc)
            xp_proc = proc.new_xpath_processor()
            xp_proc.set_context(xdm_item=docs)
            specs: list[PyXdmMap] = xp_proc.evaluate(
                f"for $el in //{self.el_spec_name} return map{{'content': $el/text(), 'name': $el/@ident/data(.)}}"
            )
            for spec in specs:
                name = spec.get("name")
                content = spec.get("content")
                if name is not None and content is not None:
                    with open(
                        self.out_dir / f"{name}.{lang}.md", "w", encoding="utf-8"
                    ) as f:
                        f.write(content.__str__())

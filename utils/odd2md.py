from pathlib import Path
from typing import Literal

import snakemd
from saxonche import PySaxonProcessor, PyXdmNode, PyXPathProcessor

from utils.main import Schema, load_config, odd_factory

LANGS = ["de", "fr", "en"]


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


class ODD2Md:
    """Convert ODD files to Markdown."""

    schema: str
    languages: list[str]
    elements: list[str]
    namespaces: list[tuple[str, str]] = [("tei", "http://www.tei-c.org/ns/1.0")]
    out_dir: Path

    def __init__(self, schema: Schema, languages: list[str], target_dir: str) -> None:
        """Initialize the class.

        Args:
            schema (Schema): The schema class instance.
            languages (list[str]): The languages to convert.
        """
        self.out_dir = Path(target_dir)
        self.languages = languages
        self.schema = schema.compiled_odd
        self.elements = self.__get_element_names()

    def __add_namespaces(self, proc: PyXPathProcessor):
        """Add the namespaces to the processor.

        Args:
            proc (PyXPathProcessor): The processor to add the namespaces to.
        """
        for prefix, uri in self.namespaces:
            proc.declare_namespace(prefix=prefix, uri=uri)

    def __create_md_doc_per_element(self, selected_lang: str, name: str):
        template = self.__generate_md_doc(title=name)
        self.__grab_description_from_element(
            selected_lang=selected_lang, name=name, doc=template
        )
        template.dump(name=f"{name}.{selected_lang}", dir=self.out_dir)

    def __grab_description_from_element(
        self, selected_lang: str, name: str, doc: snakemd.Document
    ) -> None:
        with PySaxonProcessor(license=False) as proc:
            schema_node = proc.parse_xml(xml_text=self.schema)
            xp = proc.new_xpath_processor()
            self.__add_namespaces(proc=xp)
            xp.set_context(xdm_item=schema_node)  # type: ignore
            lang_desc = xp.evaluate_single(
                f"//tei:elementSpec[@ident='{name}']/tei:desc[@xml:lang='{selected_lang}']//string()"
            )

        if lang_desc is not None:
            doc.add_paragraph(text=lang_desc.__str__())

    def __generate_md_doc(self, title: str) -> snakemd.Document:
        doc = snakemd.Document()
        doc.add_heading(text=f"{title}", level=1)
        return doc

    def __get_element_names(self) -> list[str]:
        with PySaxonProcessor(license=False) as proc:
            schema_node = proc.parse_xml(xml_text=self.schema)
            xp = proc.new_xpath_processor()
            self.__add_namespaces(proc=xp)
            xp.set_context(xdm_item=schema_node)  # type: ignore
            els = xp.evaluate("//tei:elementSpec/@ident/data(.)")
        return sorted([el.__str__() for el in els])

    def create_md_doc(self) -> None:
        for lang in self.languages:
            for element in self.elements:
                self.__create_md_doc_per_element(selected_lang=lang, name=element)

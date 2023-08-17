import xml.etree.ElementTree as ET
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from utils.docs.specs.abstract import ODDElement
from utils.docs.specs.dataspec import DataSpec
from utils.docs.specs.element import ElementSpec
from utils.docs.specs.macrospec import MacroSpec
from utils.docs.specs.ns import NS_MAP
from utils.docs.specs.odd_class import ClassSpec
from utils.docs.translater import TRANSLATE, Translations
from utils.schema.compile import Schema, load_config, odd_factory

# default languages used to generate the documentation
LANGS = ["de", "fr"]


@dataclass(frozen=True)
class ElementMdSpec:
    filename: str
    nav_title: str


def create_schema_by_entry(entry_point: str) -> Schema | None:
    """Create a schema from the config file.

    Args:
        entry_point (str): The name of the entry point.

    Returns:
        Schema | None: A schema class instance if it exists, None otherwise.
    """
    config = load_config()

    if config is None:
        return None

    schema_config = [
        schema for schema in config.schemas if schema["entry"] == entry_point
    ][0]
    return odd_factory(
        schema_config=schema_config,
        authors=config.authors,
    )


class ODDReader:
    odd: ET.Element
    elements: dict[str, ElementSpec]
    components: dict[str, ODDElement]
    translations: Translations

    def __init__(self, odd: str, translations: Translations = TRANSLATE):
        self.odd = ET.fromstring(odd)
        self.elements = {spec.ident: spec for spec in self._get_element_specs()}
        self.components = {
            component.ident: component
            for component in self._get_component_specs()
            if isinstance(component, ODDElement)
        }
        self.translations = translations

    def _get_component_specs(self) -> Iterator[ClassSpec | DataSpec | MacroSpec]:
        from itertools import chain

        class_specs = [
            ClassSpec(element=class_spec)
            for class_spec in self.odd.findall(".//tei:classSpec", namespaces=NS_MAP)
        ]
        data_specs = [
            DataSpec(element=data_spec)
            for data_spec in self.odd.findall(".//tei:dataSpec", namespaces=NS_MAP)
        ]
        macro_specs = [
            MacroSpec(element=macro_spec)
            for macro_spec in self.odd.findall(".//tei:macroSpec", namespaces=NS_MAP)
        ]
        return chain(class_specs, data_specs, macro_specs)

    def _get_element_specs(self) -> list[ElementSpec]:
        el_specs = self.odd.findall(".//tei:elementSpec", namespaces=NS_MAP)
        return [ElementSpec(element=el_spec) for el_spec in el_specs]


class ODD2Md:
    """A class which helps to streamline the process of converting ODD files to Markdown."""

    schema: ODDReader
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
        self.schema = ODDReader(
            odd=schema.compiled_odd if isinstance(schema, Schema) else schema
        )

    def create_md_doc_per_lang(self) -> list[ElementMdSpec]:
        """Create a markdown documentation per element per language.

        Returns:
            list[ElementMdSpec]: A sorted list of ElementMdSpec instances.
        """

        elements_specs_created: list[ElementMdSpec] = []

        for _, element in self.schema.elements.items():
            elements_specs_created.append(
                ElementMdSpec(filename=f"{element.ident}.md", nav_title=element.ident)
            )
            for lang in self.languages:
                element.to_markdown(
                    components=self.schema.components,
                    elements=self.schema.elements,
                    lang=lang,
                    lang_translations=getattr(self.schema.translations, lang),
                    path=self.out_dir,
                )

        return sorted(elements_specs_created, key=lambda x: x.nav_title)

from dataclasses import dataclass
from pathlib import Path

from utils.docs.oddreader import ODDReader
from utils.schema.compile import Schema, load_config, odd_factory


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

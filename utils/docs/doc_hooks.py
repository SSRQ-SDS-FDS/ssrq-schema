from pathlib import Path
from typing import Any

from mkdocs.config.defaults import MkDocsConfig  # type: ignore
from mkdocs.livereload import LiveReloadServer
from mkdocs.plugins import event_priority
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

from utils.commons import config as configs
from utils.docs.extensions.md_xi import md_xi_plugin
from utils.docs.odd2md import LANGS, ODD2Md, create_schema_by_entry
from utils.schema.compile import Schema, store_compiled_schemas

created_schema: dict[str, Schema] = {}


def create_main_schema() -> Schema:
    if created_schema.get("main") is None:
        schema = create_schema_by_entry(entry_point="main.odd.xml")
        if schema is not None:
            created_schema["main"] = schema
            return created_schema["main"]
    return created_schema["main"]


@event_priority(100)
def on_config(config: MkDocsConfig):
    schema = create_main_schema()
    odd2md = ODD2Md(
        schema=schema, languages=LANGS, target_dir=f"{config.docs_dir}/elements"
    )
    created_md_specs = odd2md.create_md_doc_per_lang()

    nav_config: list[dict[str, list[str | dict[str, str]]]] = config.nav  # type: ignore

    for nav_entry in nav_config:
        if nav_entry.get("Elements") is not None:
            for md_spec in created_md_specs:
                nav_entry["Elements"].append(
                    {md_spec.nav_title: f"elements/{md_spec.filename}"}
                )


@event_priority(50)
def on_page_markdown(
    markdown: str, config: MkDocsConfig, page: Page, files: Files
) -> str:
    return md_xi_plugin(markdown, xi_base_path=configs.EXAMPLES_DIR)


@event_priority(50)
def on_post_build(config: MkDocsConfig):
    schema = create_main_schema()
    store_compiled_schemas(schemas=[schema], out_dir=Path(config.site_dir))


@event_priority(50)
def on_serve(server: LiveReloadServer, config: MkDocsConfig, builder: Any):
    server.unwatch(config.docs_dir)

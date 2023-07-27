from typing import Any

from mkdocs.config.defaults import MkDocsConfig  # type: ignore
from mkdocs.livereload import LiveReloadServer
from mkdocs.plugins import event_priority

from utils.odd2md import LANGS, ODD2Md, create_schema_by_entry


@event_priority(50)
def on_config(config: MkDocsConfig):
    schema = create_schema_by_entry(entry_point="main.odd.xml")
    if schema is not None:
        odd2md = ODD2Md(
            schema=schema, languages=LANGS, target_dir=f"{config.docs_dir}/elements"
        )
        odd2md.create_md_doc_per_lang()


@event_priority(50)
def on_serve(server: LiveReloadServer, config: MkDocsConfig, builder: Any):
    server.unwatch(config.docs_dir)

from pathlib import Path
from typing import Optional, TypedDict

import tomllib
from pydantic import BaseModel, validator
from saxonche import PySaxonProcessor, PyXdmNode, PyXslt30Processor, PyXsltExecutable

CWD = Path.cwd()
SRC_DIR = CWD / "src"
XSLT_BASE = CWD / SRC_DIR / "xsl"
TEI_STYLESHEETS = CWD / SRC_DIR / "lib/tei_stylesheets/odds"
XSLTS = {
    "clean": XSLT_BASE / "clean-compiled.xsl",
    "meta": XSLT_BASE / "fill-meta.xsl",
    "odd2odd": TEI_STYLESHEETS / "odd2odd.xsl",
}


class SSRQSchemaType(TypedDict):
    description: str
    entry: str
    tei_version: str
    title: str
    version: str


class SSRQConfig(BaseModel):
    authors: list[str]
    schemas: list[SSRQSchemaType]

    @validator("schemas", pre=True)
    def version_issemver(cls, schemas: list[SSRQSchemaType]) -> list[SSRQSchemaType]:
        import semver

        for schema in schemas:
            if semver.VersionInfo.isvalid(schema["version"]) is False:
                raise ValueError("version must be a semantic version string")
            if semver.VersionInfo.isvalid(schema["tei_version"]) is False:
                raise ValueError(
                    "the selected tei version must be a semantic version string"
                )
        return schemas


def load_config() -> Optional[SSRQConfig]:
    with open(
        CWD / "pyproject.toml",
        "rb",
    ) as f:
        config = tomllib.load(f)

    return SSRQConfig(**config["ssrq"]["schema"]["meta"])


def fill_template_with_metadata(authors: list[str], schema: SSRQSchemaType) -> str:
    with PySaxonProcessor(license=False) as proc:
        proc.set_configuration_property(name="xi", value="on")
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(
            xml_file_name=f"{str(SRC_DIR)}/{schema['entry']}"
        )

        # the not very elegant way to pass parameters to the stylesheet...
        xsltproc.set_parameter(
            "authors",
            proc.make_array(
                [
                    proc.make_string_value(author.split("<")[0].strip())
                    for author in authors
                ]
            ),
        )
        xsltproc.set_parameter("desc", proc.make_string_value(schema["description"]))
        xsltproc.set_parameter("title", proc.make_string_value(schema["title"]))
        xsltproc.set_parameter("version", proc.make_string_value(schema["version"]))

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(
            stylesheet_file=str(XSLTS["meta"])
        )
        result = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("No result from XSLT transformation")

    return result


def compile_odd_to_odd(odd: str, tei_version: str) -> str:
    with PySaxonProcessor(license=False) as proc:
        proc.set_configuration_property(name="xi", value="on")
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=odd)
        xsltproc.set_parameter("defaultTEIVersion", proc.make_string_value(tei_version))

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(
            stylesheet_file=str(XSLTS["odd2odd"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("No result from XSLT transformation")

    return result


def odd_factory(
    schema_config: SSRQSchemaType, authors: list[str], clean: bool = True
) -> str:
    odd_with_metadata = fill_template_with_metadata(
        authors=authors, schema=schema_config
    )
    compiled_odd = compile_odd_to_odd(
        odd=odd_with_metadata, tei_version=schema_config["tei_version"]
    )

    if clean:
        with PySaxonProcessor(license=False) as proc:
            proc.set_configuration_property(name="xi", value="on")
            xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
            document: PyXdmNode = proc.parse_xml(xml_text=compiled_odd)

            xsl: PyXsltExecutable = xsltproc.compile_stylesheet(
                stylesheet_file=str(XSLTS["clean"])
            )
            result: str = xsl.transform_to_string(xdm_node=document)

        if result is None:
            raise ValueError("No result from XSLT transformation, while cleaning")

        return result

    return compiled_odd


if __name__ == "__main__":
    from functools import partial
    from multiprocessing import Pool, cpu_count

    config = load_config()
    if config is not None:
        cpus = cpu_count()
        len_schemas = len(config.schemas)
        with Pool(processes=len_schemas if len_schemas <= cpus else cpus) as p:
            odds = p.map(partial(odd_factory, authors=config.authors), config.schemas)

        for odd in odds:
            print(odd)
    else:
        print("No config found – can't continue")

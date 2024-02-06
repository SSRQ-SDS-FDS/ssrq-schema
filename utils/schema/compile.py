import re
from dataclasses import dataclass
from pathlib import Path

import tomllib
from pydantic import BaseModel, field_validator
from saxonche import PySaxonProcessor, PyXdmNode, PyXslt30Processor, PyXsltExecutable
from typing_extensions import TypedDict

import utils.commons.config as configs
import utils.commons.filehandler as io
from utils.commons.logger import LOGGER
from utils.schema import steps

OMIT_VERSION: bool = False

SPECIFIED_ELEMENTS = r'target="elements/(\w+)\.xml"'


class SSRQSchemaType(TypedDict):
    description: str
    entry: str
    tei_version: str
    name: str
    title: str
    version: str


class SSRQConfig(BaseModel):
    authors: list[str]
    schemas: list[SSRQSchemaType]

    @field_validator("schemas", mode="before")
    @classmethod
    def version_issemver(cls, schemas: list[SSRQSchemaType]) -> list[SSRQSchemaType]:
        import semver  # type: ignore

        for schema in schemas:
            if semver.VersionInfo.is_valid(schema["version"]) is False:
                raise ValueError("version must be a semantic version string")
            if semver.VersionInfo.is_valid(schema["tei_version"]) is False:
                raise ValueError(
                    "the selected tei version must be a semantic version string"
                )
        return schemas


@dataclass
class Schema:
    version: str
    name: str
    compiled_odd: str
    rng: str


def store_compiled_schemas(
    schemas: list[Schema],
    io: io.AbstractFileHandler = io.FileHandler,
    out_dir: Path = configs.BUILD_DIR,
    omit_version: bool = OMIT_VERSION,
) -> None:
    for schema in schemas:
        odd_name = (
            f"{schema.name}{f'_{schema.version}' if omit_version is False else ''}.odd"
        )
        rng_name = (
            f"{schema.name}{f'_{schema.version}' if omit_version is False else ''}.rng"
        )

        io.write(directory=out_dir, file_name=odd_name, content=schema.compiled_odd)
        io.write(directory=out_dir, file_name=rng_name, content=schema.rng)


def load_config(io: io.AbstractFileHandler = io.FileHandler) -> SSRQConfig:
    pyproject_toml = tomllib.loads(
        io.read(directory=configs.PROJECT_DIR, file_name="pyproject.toml")
    )

    return SSRQConfig(**pyproject_toml["ssrq"]["schema"]["meta"])


def resolve_relative_paths(doc: str) -> str:
    """A small helper function to replace relative @target paths with absolute paths.
    It would be an alternative approach to use the saxon set_base_uri() method, but this
    method has some strange behaviours."""

    with PySaxonProcessor(license=False) as proc:
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=doc)
        xsltproc.set_parameter(  # type: ignore
            "path_base",
            proc.make_string_value(configs.SCHEMA_DIR.absolute().as_uri()),  # type: ignore
        )

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(configs.XSLTS["path"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("Failed to resolve relative paths")

    return result


def resolve_specs(doc: str) -> str:
    with PySaxonProcessor(license=False) as proc:
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=doc)

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(configs.XSLTS["specs"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("Failed to include tei:specGrpRefs")

    return result


def resolve_xincludes(doc: str) -> str:
    with PySaxonProcessor(license=False) as proc:
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=doc)
        xsltproc.set_parameter(  # type: ignore
            "path_base",
            proc.make_string_value(configs.EXAMPLES_DIR.absolute().as_uri()),  # type: ignore
        )

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(configs.XSLTS["xi"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("Failed to resolve xincludes")

    return result


def resolve_embedded_spec_files(doc: str) -> str:
    """A helper function, which first resolves the content of all embeddes specs and then resolves the
    examples embedded via xinclude."""

    result_specs = resolve_specs(doc=doc)
    return resolve_xincludes(doc=result_specs)


def check_embedded_files(doc: str, schema: SSRQSchemaType) -> None:
    """A helper function to check if all files, which are embedded in the ODD file via specGrpRef
    are available in the src directory. If not, an error is raised."""

    from os.path import exists
    from urllib.parse import urlparse

    embedded_files = re.findall(r'specGrpRef target="(.*\.xml)(?:.*)?"', doc)

    try:
        bundled_exceptions = []
        for file in embedded_files:
            if exists(urlparse(file).path):
                continue
            bundled_exceptions.append(FileNotFoundError(f"{file} not found"))
        if len(bundled_exceptions) > 0:
            raise ExceptionGroup("File not found", bundled_exceptions)
    except ExceptionGroup as errors:
        print(
            f"The following files in schema {schema['entry']} are missing – fix the paths before you continue:"
        )
        for e in errors.exceptions:
            print(e)

        raise SystemExit(1)


def fill_template_with_metadata(authors: list[str], schema: SSRQSchemaType) -> str:
    with PySaxonProcessor(license=False) as proc:
        proc.set_configuration_property(name="xi", value="on")  # type: ignore
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(
            xml_file_name=f"{str(configs.SCHEMA_DIR)}/{schema['entry']}"
        )

        xsltproc.set_parameter(
            "description", proc.make_string_value(schema["description"])
        )  # type: ignore
        xsltproc.set_parameter("title", proc.make_string_value(schema["title"]))  # type: ignore
        xsltproc.set_parameter("version", proc.make_string_value(schema["version"]))  # type: ignore

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(configs.XSLTS["meta"])
        )
        result = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("No result from XSLT transformation")

    return result


def compile_odd_to_odd(odd: str, tei_version: str) -> str:
    with PySaxonProcessor(license=False) as proc:
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=odd)
        xsltproc.set_parameter("defaultTEIVersion", proc.make_string_value(tei_version))  # type: ignore

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(configs.XSLTS["odd2odd"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("No result from XSLT transformation")

    return result


def resolve_sch_let(odd: str) -> str:
    with PySaxonProcessor(license=False) as proc:
        proc.set_configuration_property(name="xi", value="on")  # type: ignore
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=odd)

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(configs.XSLTS["vars"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("No result from XSLT transformation, while cleaning")

    return result


def compile_odd_to_rng(odd: str, tei_version: str) -> str:
    with PySaxonProcessor(license=False) as proc:
        proc.set_configuration_property(name="xi", value="on")  # type: ignore
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=odd)
        xsltproc.set_parameter("defaultTEIVersion", proc.make_string_value(tei_version))  # type: ignore

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(configs.XSLTS["odd2rng"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("No result from XSLT transformation")

    return result


def odd_factory(
    schema_config: SSRQSchemaType,
    authors: list[str],
    clean: bool = True,
    print_stats: bool = False,
) -> Schema:
    LOGGER.info(f'Compiling schema {schema_config["entry"]}')

    odd_with_metadata = fill_template_with_metadata(
        authors=authors, schema=schema_config
    )

    if print_stats:
        steps.Stats()(odd_with_metadata)

    odd_with_metadata = resolve_relative_paths(doc=odd_with_metadata)

    check_embedded_files(doc=odd_with_metadata, schema=schema_config)

    odd_resolved_specs = resolve_embedded_spec_files(doc=odd_with_metadata)

    compiled_odd = compile_odd_to_odd(
        odd=odd_resolved_specs, tei_version=schema_config["tei_version"]
    )

    if clean:
        with PySaxonProcessor(license=False) as proc:
            proc.set_configuration_property(name="xi", value="on")  # type: ignore
            xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
            document: PyXdmNode = proc.parse_xml(xml_text=compiled_odd)

            xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
                stylesheet_file=str(configs.XSLTS["clean"])
            )
            result: str = xsl.transform_to_string(xdm_node=document)

        if result is None:
            raise ValueError("No result from XSLT transformation, while cleaning")

        compiled_odd = result

    compiled_odd = resolve_sch_let(odd=compiled_odd)

    rng = compile_odd_to_rng(odd=compiled_odd, tei_version=schema_config["tei_version"])

    return Schema(
        version=schema_config["version"],
        name=schema_config["name"],
        compiled_odd=compiled_odd,
        rng=rng,
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--omit-version", type=bool, default=False)
    args = parser.parse_args()

    if args.omit_version:
        OMIT_VERSION = args.omit_version

    config = load_config()
    len_schemas = len(config.schemas)
    odds = [
        odd_factory(schema_config=schema, authors=config.authors, print_stats=True)
        for schema in config.schemas
    ]

    for odd in odds:
        store_compiled_schemas(schemas=[odd], omit_version=OMIT_VERSION)

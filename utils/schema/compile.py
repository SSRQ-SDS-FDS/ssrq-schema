import re
from dataclasses import dataclass
from pathlib import Path

import tomllib
from pydantic import BaseModel, field_validator
from saxonche import PySaxonProcessor, PyXdmNode, PyXslt30Processor, PyXsltExecutable
from typing_extensions import TypedDict

import utils.commons.config as configs

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
            if semver.VersionInfo.isvalid(schema["version"]) is False:
                raise ValueError("version must be a semantic version string")
            if semver.VersionInfo.isvalid(schema["tei_version"]) is False:
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

    def store(self, out_dir: Path = configs.BUILD_DIR) -> None:
        """Store the compiled ODD and RNG files in the dist directory – the version number is omitted if OMIT_VERSION is True."""
        from os import makedirs
        from os.path import exists

        if not exists(out_dir):
            makedirs(out_dir)

        with open(
            f"{out_dir}/{self.name}{f'_{self.version}' if OMIT_VERSION is False else ''}.odd",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(self.compiled_odd)
        with open(
            f"{out_dir}/{self.name}{f'_{self.version}' if OMIT_VERSION is False else ''}.rng",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(self.rng)


def load_config() -> SSRQConfig | None:
    """Load the configuration from pyproject.toml and apply some basic validation using pydantic."""
    with open(
        configs.PROJECT_DIR / "pyproject.toml",
        "rb",
    ) as f:
        config = tomllib.load(f)

    return SSRQConfig(**config["ssrq"]["schema"]["meta"])


def resolve_relative_paths(doc: str) -> str:
    """A small helper function to replace relative @target paths with absolute paths.
    It would be an alternative approach to use the saxon set_base_uri() method, but this
    method has some strange behaviours."""

    with PySaxonProcessor(license=False) as proc:
        xsltproc: PyXslt30Processor = proc.new_xslt30_processor()
        document: PyXdmNode = proc.parse_xml(xml_text=doc)
        xsltproc.set_parameter(  # type: ignore
            "path_base", proc.make_string_value(configs.SCHEMA_DIR.absolute().as_uri())  # type: ignore
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
            "path_base", proc.make_string_value(configs.EXAMPLES_DIR.absolute().as_uri())  # type: ignore
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


def show_stats(schema: str, filename: str) -> None:
    included_elements = calculate_number_of_included_elements(schema)
    specified_elements = calculate_number_of_specified_elements(schema)
    print_stats(filename, included_elements, specified_elements)


def calculate_number_of_included_elements(schema) -> int:
    include_list = re.findall(r'include="(.*)"', schema)
    include_string = " ".join(include_list)
    include_string = re.sub(r"(\s)+", " ", include_string)
    include_list = include_string.split(" ")
    return len(include_list)


def calculate_number_of_specified_elements(schema) -> int:
    specified_list = re.findall(SPECIFIED_ELEMENTS, schema)
    return len(specified_list)


def print_stats(filename: str, included_elements: int, specified_elements: int) -> None:
    print(
        f"Elements included in {filename}: {included_elements}\n"
        f"Elements already specified: {specified_elements}\n"
        f"Elements to specify: {included_elements - specified_elements}\n"
    )


def odd_factory(
    schema_config: SSRQSchemaType,
    authors: list[str],
    clean: bool = True,
    print_stats: bool = False,
) -> Schema:
    odd_with_metadata = fill_template_with_metadata(
        authors=authors, schema=schema_config
    )

    if print_stats:
        show_stats(schema=odd_with_metadata, filename=schema_config["entry"])

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
    if config is not None:
        len_schemas = len(config.schemas)
        odds = [
            odd_factory(schema_config=schema, authors=config.authors, print_stats=True)
            for schema in config.schemas
        ]

        for odd in odds:
            odd.store()
    else:
        print("No config found – can't continue")

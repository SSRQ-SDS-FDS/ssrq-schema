import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import tomllib
from saxonche import PySaxonProcessor, PyXdmNode, PyXslt30Processor, PyXsltExecutable

from utils.SSRQConfig import SSRQConfig
from utils.SSRQSchemaType import SSRQSchemaType

CUR_DIR = Path(__file__).parent.parent.absolute()
DIST_DIR = CUR_DIR / "dist"
SRC_DIR = CUR_DIR / "src"
EXAMPLES_DIR = SRC_DIR / "examples"
COMMON_DIR = SRC_DIR / "common"
ELEMENTS_DIR = SRC_DIR / "elements"
XSLT_BASE = CUR_DIR / SRC_DIR / "xsl"
TEI_STYLESHEETS = CUR_DIR / SRC_DIR / "lib/tei_stylesheets/odds"
XSLTS = {
    "change-start": XSLT_BASE / "change-rng-start.xsl",
    "clean": XSLT_BASE / "clean-compiled.xsl",
    "meta": XSLT_BASE / "fill-meta.xsl",
    "odd2odd": TEI_STYLESHEETS / "odd2odd.xsl",
    "odd2rng": TEI_STYLESHEETS / "odd2relax.xsl",
    "path": XSLT_BASE / "resolve-path.xsl",
    "specs": XSLT_BASE / "resolve-specs.xsl",
    "vars": XSLT_BASE / "resolve-sch-let.xsl",
    "xi": XSLT_BASE / "resolve-xi.xsl",
}
OMIT_VERSION: bool = False

SPECIFIED_ELEMENTS = r'target="elements/(\w+)\.xml"'


@dataclass
class Schema:
    version: str
    name: str
    compiled_odd: str
    rng: str

    def store(self) -> None:
        """Store the compiled ODD and RNG files in the dist directory – the version number is omitted if OMIT_VERSION is True."""
        from os import makedirs
        from os.path import exists

        if not exists(DIST_DIR):
            makedirs(DIST_DIR)

        with open(
            f"{DIST_DIR}/{self.name}{f'_{self.version}' if OMIT_VERSION is False else ''}.odd",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(self.compiled_odd)
        with open(
            f"{DIST_DIR}/{self.name}{f'_{self.version}' if OMIT_VERSION is False else ''}.rng",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(self.rng)


def load_config() -> Optional[SSRQConfig]:
    """Load the configuration from pyproject.toml and apply some basic validation using pydantic."""
    with open(
        CUR_DIR / "pyproject.toml",
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
            "path_base", proc.make_string_value(SRC_DIR.absolute().as_uri())  # type: ignore
        )

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(XSLTS["path"])
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
            stylesheet_file=str(XSLTS["specs"])
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
            "path_base", proc.make_string_value(EXAMPLES_DIR.absolute().as_uri())  # type: ignore
        )

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(XSLTS["xi"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("Failed to resolve xincludes")

    return result


def resolve_embedded_spec_files(doc: str) -> str:
    """A helper function, which first resolves the content of all embeddes specs and then resolves the
    examples embedded via xinclude."""

    result_specs = resolve_specs(doc=doc)
    result_xi = resolve_xincludes(doc=result_specs)

    return result_xi


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
            xml_file_name=f"{str(SRC_DIR)}/{schema['entry']}"
        )

        # the not very elegant way to pass parameters to the stylesheet...
        xsltproc.set_parameter(  # type: ignore
            "authors",
            proc.make_array(  # type: ignore
                [
                    proc.make_string_value(author.split("<")[0].strip())  # type: ignore
                    for author in authors
                ]
            ),
        )
        xsltproc.set_parameter("desc", proc.make_string_value(schema["description"]))  # type: ignore
        xsltproc.set_parameter("title", proc.make_string_value(schema["title"]))  # type: ignore
        xsltproc.set_parameter("version", proc.make_string_value(schema["version"]))  # type: ignore

        xsl: PyXsltExecutable = xsltproc.compile_stylesheet(  # type: ignore
            stylesheet_file=str(XSLTS["meta"])
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
            stylesheet_file=str(XSLTS["odd2odd"])
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
            stylesheet_file=str(XSLTS["vars"])
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
            stylesheet_file=str(XSLTS["odd2rng"])
        )
        result: str = xsl.transform_to_string(xdm_node=document)

    if result is None:
        raise ValueError("No result from XSLT transformation")

    return result


def show_stats(schema: str, name: str) -> None:
    included_elements: list[str] = " ".join(
        re.findall(r'include="(.*)"', schema)
    ).split(" ")
    specified_elements: list[str] = re.findall(SPECIFIED_ELEMENTS, schema)
    print(
        f"Elements included in {name}: {len(included_elements)}\nElements already specified: {len(specified_elements)}\nElements to specify: {len(included_elements) - len(specified_elements)}\n"
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
        show_stats(schema=odd_with_metadata, name=schema_config["entry"])

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
                stylesheet_file=str(XSLTS["clean"])
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

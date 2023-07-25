from typing import Optional

import tomllib

from utils.constants import (
    EXAMPLES_DIR,
    PROJECT_DIR,
    SRC_DIR,
    XSLTS,
)
from utils.odd_pipeline.factory import ODDFactory
from utils.oddstats import AnalyzeStats, Stats
from utils.ssrqconfig import SSRQConfig
from utils.validate import ValidatePaths, Validator
from utils.xslt import XSLT, XSLTApplier, XSLTParam


def load_config() -> Optional[SSRQConfig]:
    """Load the configuration from pyproject.toml and apply some basic validation using pydantic."""
    with open(
        PROJECT_DIR / "pyproject.toml",
        "rb",
    ) as f:
        config = tomllib.load(f)

    return SSRQConfig(**config["ssrq"]["schema"]["meta"])


COMPILE_ODD_STEPS: list[XSLT | Stats | Validator] = [
    XSLTApplier(
        stylesheet=str(XSLTS["xi"]),
        requires=None,
        params=XSLTParam("path_base", SRC_DIR.absolute().as_uri()),
        config=None,
        step_name="resolve-xincludes",
    ),
    XSLTApplier(
        stylesheet=str(XSLTS["meta"]),
        requires=["authors"],
        params=None,
        config=None,
        step_name="fill-header-with-metadata",
    ),
    AnalyzeStats(),
    XSLTApplier(
        stylesheet=str(XSLTS["path"]),
        requires=None,
        params=XSLTParam("path_base", SRC_DIR.absolute().as_uri()),
        config=None,
        step_name="resolve-relativ-paths",
    ),
    ValidatePaths(),
    XSLTApplier(
        stylesheet=str(XSLTS["specs"]),
        requires=None,
        params=None,
        config=None,
        step_name="resolve-specs",
    ),
    XSLTApplier(
        stylesheet=str(XSLTS["xi"]),
        requires=None,
        params=XSLTParam("path_base", EXAMPLES_DIR.absolute().as_uri()),
        config=None,
        step_name="resolve-xincludes",
    ),
    XSLTApplier(
        stylesheet=str(XSLTS["odd2odd"]),
        requires=["defaultTEIVersion"],
        params=None,
        config=None,
        step_name="odd2odd",
    ),
    XSLTApplier(
        stylesheet=str(XSLTS["clean"]),
        requires=None,
        params=None,
        config=None,
        step_name="clean",
    ),
    XSLTApplier(
        stylesheet=str(XSLTS["vars"]),
        requires=None,
        params=None,
        config=None,
        step_name="resolve-sch-let",
    ),
]

RNG_STEP: XSLT = XSLTApplier(
    stylesheet=str(XSLTS["odd2rng"]),
    requires=["defaultTEIVersion"],  # not sure if this is needed
    params=None,
    config=None,
    step_name="odd2rng",
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
        for schema in config.schemas:
            odd = ODDFactory(authors=config.authors, schema_config=schema).create(
                compile_odd_steps=COMPILE_ODD_STEPS,
                create_rng=RNG_STEP,
            )
            odd.store()
    else:
        print("No config found – can't continue")

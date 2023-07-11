from typing import Optional

import tomllib

from utils.constants import (
    CUR_DIR,
)
from utils.oddfactory import ODDFactory
from utils.ssrqconfig import SSRQConfig


def load_config() -> Optional[SSRQConfig]:
    """Load the configuration from pyproject.toml and apply some basic validation using pydantic."""
    with open(
        CUR_DIR / "pyproject.toml",
        "rb",
    ) as f:
        config = tomllib.load(f)

    return SSRQConfig(**config["ssrq"]["schema"]["meta"])


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
            ODDFactory.create(
                schema_config=schema, authors=config.authors, print_stats=True
            )
            for schema in config.schemas
        ]

        for odd in odds:
            odd.store()
    else:
        print("No config found – can't continue")

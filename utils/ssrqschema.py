from dataclasses import dataclass

from utils.constants import DIST_DIR

OMIT_VERSION: bool = False


@dataclass
class SSRQSchema:
    version: str
    name: str
    compiled_odd: str
    rng: str

    def store(self) -> None:
        """Store the compiled ODD and RNG files in the dist directory –
        the version number is omitted if OMIT_VERSION is True."""
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

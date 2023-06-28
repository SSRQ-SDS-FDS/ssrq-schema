from json import load
from pathlib import Path

from pydantic import BaseModel, root_validator

translations_file = Path(__file__).parent.parent / "docs/translations/translations.json"


class Translations(BaseModel):
    de: dict[str, str]
    fr: dict[str, str]

    @root_validator
    def check_translation_keys(cls, values):
        from itertools import combinations

        vals = values.get("de"), values.get("fr")
        for a, b in combinations(vals, 2):
            try:
                assert a.keys() == b.keys()
            except AssertionError:
                key_diff = set(a.keys()) - set(b.keys())
                raise ValueError(
                    f"The keys of the translations must be the same for all languages. Found the following difference: {key_diff}"
                )
        return values


with open(translations_file) as f:
    content = load(f)

TRANSLATE = Translations(**content)

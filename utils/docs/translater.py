from json import load

from pydantic import BaseModel, model_validator

from utils.commons.config import SRC_DIR

translations_file = SRC_DIR / "docs/translations/translations.json"


class Translations(BaseModel):
    de: dict[str, str]
    fr: dict[str, str]

    @model_validator(mode="after")
    def check_translation_keys(self):
        from itertools import combinations

        vals = self.de, self.fr
        for a, b in combinations(vals, 2):
            try:
                assert a.keys() == b.keys()
            except AssertionError:
                key_diff = set(a.keys()) - set(b.keys())
                raise ValueError(
                    f"The keys of the translations must be the same for all languages. Found the following difference: {key_diff}"
                )
        return self


with open(translations_file) as f:
    content = load(f)

TRANSLATE = Translations(**content)

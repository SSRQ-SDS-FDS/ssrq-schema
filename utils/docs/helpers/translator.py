from json import loads

from pydantic import BaseModel, model_validator

from utils.commons import filehandler as io
from utils.commons.config import SRC_DIR

translations_file = "docs/translations/translations.json"
translations = io.FileHandler.read(directory=SRC_DIR, file_name=translations_file)


class Translator(BaseModel):
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


TRANSLATE = Translator(**loads(translations))

from utils.constants import SRC_DIR
from utils.oddstats import Stats
from utils.ssrqschema import SSRQSchema
from utils.ssrqschematype import SSRQSchemaType
from utils.validate import Validator
from utils.xslt import XSLT, XSLTParam, XSLTParamList


class ODDFactory:
    authors: list[str]
    name: str
    entry: str
    version: str
    defaultTEIVersion: str

    def __init__(
        self,
        authors: list[str],
        schema_config: SSRQSchemaType,
    ):
        self.authors = authors
        self.name = schema_config["name"]
        self.version = schema_config["version"]
        self.entry = schema_config["entry"]
        self.defaultTEIVersion = schema_config["tei_version"]

    def create(
        self,
        compile_odd_steps: list[XSLT | Validator | Stats],
        create_rng: XSLT,
    ) -> SSRQSchema:
        compiled_odd: str = ODDFactory.open_schema(name=self.entry)

        for step in compile_odd_steps:
            if isinstance(step, XSLT):
                if step.requires is not None:
                    for requirement in step.requires:
                        info: list[str] | str | None = (
                            getattr(self, requirement)
                            if hasattr(self, requirement)
                            else None
                        )
                        if info is not None:
                            step.add_params_from_pipe(
                                params=XSLTParamList(
                                    name=requirement,
                                    value=[
                                        XSLTParam(name="name", value=i) for i in info
                                    ],
                                )
                                if isinstance(info, list)
                                else XSLTParam(name=requirement, value=info)
                            )

                compiled_odd = step.apply(doc=compiled_odd)
            elif isinstance(step, Validator):
                step.validate(doc=compiled_odd, name=self.name)
            elif isinstance(step, Stats):
                step.show_stats(schema=compiled_odd, name=self.name)

        return SSRQSchema(
            version=self.version,
            name=self.name,
            compiled_odd=compiled_odd,
            rng=create_rng.apply(doc=compiled_odd),
        )

    @staticmethod
    def open_schema(name: str) -> str:
        with open(f"{str(SRC_DIR)}/{name}", "r", encoding="utf-8") as f:
            return f.read()

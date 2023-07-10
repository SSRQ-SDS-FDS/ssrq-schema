from pydantic import BaseModel, validator

from utils.SSRQSchemaType import SSRQSchemaType


class SSRQConfig(BaseModel):
    authors: list[str]
    schemas: list[SSRQSchemaType]

    @validator("schemas", pre=True)
    def version_issemver(self, schemas: list[SSRQSchemaType]) -> list[SSRQSchemaType]:
        import semver  # type: ignore

        for schema in schemas:
            if semver.VersionInfo.isvalid(schema["version"]) is False:
                raise ValueError("version must be a semantic version string")
            if semver.VersionInfo.isvalid(schema["tei_version"]) is False:
                raise ValueError(
                    "the selected tei version must be a semantic version string"
                )
        return schemas

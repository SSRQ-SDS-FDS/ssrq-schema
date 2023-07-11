from pydantic import BaseModel, validator

from utils.ssrqschematype import SSRQSchemaType


class SSRQConfig(BaseModel):
    authors: list[str]
    schemas: list[SSRQSchemaType]

    @validator("authors")
    def remove_mail_from_authors(cls, authors: list[str]) -> list[str]:
        return [
            author.split("<")[0].strip() if "@" in author else author
            for author in authors
        ]

    @validator("schemas", pre=True)
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

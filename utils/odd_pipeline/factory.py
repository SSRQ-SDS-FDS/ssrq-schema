from utils.constants import SRC_DIR
from utils.helpers.reader import FileReader, Reader
from utils.odd_pipeline.step import Step
from utils.ssrqschema import SSRQSchema
from utils.ssrqschematype import SSRQSchemaType


def odd_to_schema(
    config: SSRQSchemaType,
    compile_odd_steps: list[Step],
    create_rng: Step,
    file_reader: Reader = FileReader(),
) -> SSRQSchema:
    """
    Compile the ODD file. This function creates a compiled ODD file and an RNG schema.

    Args:
        config (SSRQSchemaType): The configuration of the SSRQ schema.
        compile_odd_steps (list[Step]): A list of steps to apply to the ODD file.
        create_rng (Step): A step to create the RNG schema.
        file_reader (Reader, optional): A reader to read the ODD file. Defaults to FileReader().

    Returns:
        SSRQSchema: The compiled schema.
    """
    from functools import reduce

    odd_source: str = file_reader.read(f"{str(SRC_DIR)}/{self.name}")

    # This performs the actual compilation of the ODD file by applying the steps in the pipeline.
    compiled_odd: str = reduce(
        lambda value, step: step.apply(doc=value),
        compile_odd_steps,
        odd_source,
    )

    return SSRQSchema(
        version=config.version,
        name=config.name,
        compiled_odd=compiled_odd,
        rng=create_rng.apply(doc=compiled_odd),
    )

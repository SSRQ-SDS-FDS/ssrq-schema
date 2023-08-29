import logging

from rich import logging as rich_logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[rich_logging.RichHandler()],
    )

    return logging.getLogger("rich")


LOGGER = setup_logger()

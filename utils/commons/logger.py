import logging

from rich import logging as rich_logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[rich_logging.RichHandler()],
    )

    # disable snakemd logger by setting it to ERROR
    snakemd_logger = logging.getLogger("snakemd")
    snakemd_logger.setLevel(logging.ERROR)

    return logging.getLogger("rich")


LOGGER = setup_logger()

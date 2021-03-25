import logging
from typing import Union

from src.lib.config import Config


def setup_logger(name: str, config: Union[Config]) -> logging.Logger:
    logging.basicConfig(
        format=config.logging_format,
        level=config.logging_level,
    )
    return logging.getLogger(name)

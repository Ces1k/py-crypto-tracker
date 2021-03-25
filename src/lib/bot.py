import logging
from pathlib import Path
from typing import Union

from src.lib.config import Config
from src.lib.retriever import send_request

MODULE_LOGGER = logging.getLogger(Path(__file__).name)


def send_message_to_telegram(config: Union[Config], message: str) -> None:
    """Send message to Telegram
    Arguments:
        - config
        - message
    """
    url = config.telegram_bot_api
    params = {
        "chat_id": config.chat_id,
        "text": message,
    }
    send_request(url, params=params)
    MODULE_LOGGER.debug("Message sent.")

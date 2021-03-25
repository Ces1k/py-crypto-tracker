import logging
from pathlib import Path

from src.lib import utils

MODULE_LOGGER = logging.getLogger(Path(__file__).name)


LOGGING_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "errors": logging.ERROR,
    "critical": logging.CRITICAL,
}


class Config(object):
    def __init__(self, config_path="local_config.yaml"):
        self.config = self.load_config(config_path)
        # General settings
        self.logging = self.config["logging"]
        self.threshold = self.config["threshold"]
        self.request_time_interval = self.config["request_time_interval"]
        # Coinmarket API settings
        self.api_key = self.config["api_key"]
        self.cryptocurrency_listings_latest_url = self.config["cryptocurrency_listings_latest_url"]
        self.cryptocurrency_quotes_latest_url = self.config["cryptocurrency_quotes_latest_url"]
        # Telegram bot settings
        self.bot_token = self.config["bot_token"]
        self.chat_id = self.config["chat_id"]
        self.telegram_bot_api = self.config["telegram_bot_api"].format(bot_token=self.bot_token)
        # Logging settings
        self.logging_level = LOGGING_LEVELS[self.logging]
        self.set_logging_format()

    @staticmethod
    def load_config(config_path):
        try:
            MODULE_LOGGER.debug("Loading config...")
            return utils.load_yaml(utils.get_root_dir().joinpath(config_path))
        except FileNotFoundError:
            MODULE_LOGGER.error(f"{config_path} not found!")

    def set_logging_format(self):
        if self.logging == "info":
            self.logging_format = "%(message)s"
        else:
            self.logging_format = "%(asctime)s - %(name)s:%(lineno)d - %(levelname)s: %(message)s"

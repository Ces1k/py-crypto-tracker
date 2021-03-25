import pytest

from src.lib.config import Config
from tests.common import get_test_data_root_dir


class TestConfig:
    @pytest.fixture
    def expected(self):
        return {
            "logging": "debug",
            "threshold": 30000,
            "request_time_interval": 300,
            "api_key": "12345678-1234-1234-1234-123456789012",
            "cryptocurrency_listings_latest_url": "test_cryptocurrency_listings_latest_url",
            "cryptocurrency_quotes_latest_url": "test_cryptocurrency_quotes_latest_url",
            "bot_token": "1234567890:ABCDEFGHIJKLMNOPQRSUTVWXYZ123456789",
            "chat_id": "-123456789",
            "telegram_bot_api": "test_telegram_bot_api",
        }

    def test_config(self, expected):
        test_config = Config(config_path=get_test_data_root_dir().joinpath("test_config.yaml"))
        assert expected["logging"] == test_config.logging
        assert expected["threshold"] == test_config.threshold
        assert expected["request_time_interval"] == test_config.request_time_interval
        assert expected["api_key"] == test_config.api_key
        assert expected["cryptocurrency_listings_latest_url"] == test_config.cryptocurrency_listings_latest_url
        assert expected["cryptocurrency_quotes_latest_url"] == test_config.cryptocurrency_quotes_latest_url
        assert expected["bot_token"] == test_config.bot_token
        assert expected["chat_id"] == test_config.chat_id
        assert expected["telegram_bot_api"] == test_config.telegram_bot_api

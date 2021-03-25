import pytest

from src.lib import utils
from tests.common import get_test_data_root_dir


class TestGetRootDir:
    def test_get_root_dir(self):
        root = utils.get_root_dir()
        assert root.__str__().endswith("py-crypto-tracker")


class TestLoadYaml:
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

    def test_load_yaml(self, expected):
        assert expected == utils.load_yaml(get_test_data_root_dir().joinpath("test_config.yaml"))

import pytest

from src.coins import btc, eth
from src.lib.config import Config
from src.lib.retriever import get_current_price
from tests.common import get_test_data_root_dir


class TestGetCurrentPrice:
    test_data = [
        (
            Config(config_path=get_test_data_root_dir().joinpath("test_config.yaml")),
            btc.BTC(),
            '{"data": {"1": {"quote": {"USD": {"price": "123456.78"}}}}}',
            "123456.78"
        ),
        (
            Config(config_path=get_test_data_root_dir().joinpath("test_config.yaml")),
            eth.ETH(),
            '{"data": {"1027": {"quote": {"USD": {"price": "1234.56"}}}}}',
            "1234.56"
        ),
        (
            Config(config_path=get_test_data_root_dir().joinpath("test_config.yaml")),
            eth.ETH(),
            None,
            None
        ),
    ]

    @pytest.mark.parametrize("config, coin, mocked_response, expected", test_data)
    def test_get_current_price(self, mocker, config, coin, mocked_response, expected):
        mocker.patch("src.lib.retriever.send_request", return_value=mocked_response)
        assert expected == get_current_price(config=config, coin=coin)

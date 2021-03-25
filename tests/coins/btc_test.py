import pytest

from src.coins.btc import BTC


class TestBTC:
    test_data = [("1", "id"), ("btc", "symbol")]

    @pytest.fixture
    def btc(self):
        return BTC()

    @pytest.mark.parametrize("expected, attribute", test_data)
    def test_btc(self, btc, expected, attribute):
        assert expected == getattr(btc, attribute)

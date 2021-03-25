import pytest

from src.coins.eth import ETH


class TestETH:
    test_data = [("1027", "id"), ("eth", "symbol")]

    @pytest.fixture
    def eth(self):
        return ETH()

    @pytest.mark.parametrize("expected, attribute", test_data)
    def test_eth(self, eth, expected, attribute):
        assert expected == getattr(eth, attribute)

from src.coins.base import Coin


class BTC(Coin):
    def __init__(self, id="1", symbol="btc"):
        super().__init__(id=id, symbol=symbol)

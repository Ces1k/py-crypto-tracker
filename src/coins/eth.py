from src.coins.base import Coin


class ETH(Coin):
    def __init__(self, id="1027", symbol="eth"):
        super().__init__(id=id, symbol=symbol)

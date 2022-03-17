
from stock.strategy.abstract_market_strategy import AbstractMarketStrategy

class RsOnline(AbstractMarketStrategy):

    def getStock(self):
        print("RS_online getstock")
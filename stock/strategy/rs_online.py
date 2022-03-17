
from stock.strategy.abstract_market_strategy import AbstractMarketStrategy
import requests
from bs4 import BeautifulSoup

class RsOnline(AbstractMarketStrategy):

    def getStock(self,url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content)
        div = soup.find("div", {"class": "sc-kEYyzF eXKmPA"})
        stock = int(str(div).split(">")[1].split('<')[0])
        return stock

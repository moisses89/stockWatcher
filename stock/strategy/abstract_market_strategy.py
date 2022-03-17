

class AbstractMarketStrategy():

    def __init__(self,context):
        self.context = context


    def getStock(self,url):
        raise NotImplemented

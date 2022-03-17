

class AbstractMarketStrategy():

    def __init__(self,context):
        self.context = context


    def getStock(self):
        raise NotImplemented

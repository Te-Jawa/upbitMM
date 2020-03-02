from upbitpy import Upbitpy

    
class MarketSearcher:
    def __init__(self):
        self.upbit = Upbitpy()
        self.markets = self.upbit.get_market_all()
        self.KRWmarkets = []
        self.BTCmarkets = [] 
        self.USDmarkets = []

        for market in markets:
            self.pair = market['market']
            self.marketname = pair[0:3]
            if self.marketname == 'BTC':
                self.BTCmarkets.append(pair)
            elif self.marketname == 'KRW':
                self.KRWmarkets.append(pair)
            else:
                self.USDmarkets.append(pair)


        
    def get_market_spread(self, makret): #market parameter must be list
        orderbook = upbit.get_orderbook(market)
        surfaceorder = orderbook[0]['orderbook_units'][0]
        spread = (surfaceorder['ask_price'] - surfaceorder['bid_price']) / surfaceorder['ask_price']
        return spread



    def get_mininum_tick(self, price):
        if price <= 10:
            return 0.01
        elif price <= 100:
            return 0.1
        elif price <= 1000:
            return 1
        elif price <= 10000:
            return 5
        elif price <= 100000:
            return 10
        elif price <= 5000000:
            return 50
        elif price <= 1000000:
            return 100
        elif price <= 2000000:
            return 500
        else:
            return 1000

class MarketMaker:
    def __init__(self):
        self.market = MarketSearcher()

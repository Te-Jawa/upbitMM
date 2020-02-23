from upbitpy import Upbitpy

upbit = Upbitpy()
markets = upbit.get_market_all()
KRWmarkets = []
BTCmarkets = [] 
USDmarkets = []

for market in markets:
    pair = market['market']
    marketname = pair[0:3]
    if marketname == 'BTC':
        BTCmarkets.append(pair)
    elif marketname == 'KRW':
        KRWmarkets.append(pair)
    else:
        USDmarkets.append(pair)
    
print(BTCmarkets)
print(KRWmarkets)
print(USDmarkets)

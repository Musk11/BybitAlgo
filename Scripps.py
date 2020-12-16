import bybit
client = bybit.bybit(test=False, api_key="YTK4qVhUVIBKybiu46", api_secret="35XX8vNcuzl4oMBiujdjOaoeeMVvhuX0R18t")
btcusdInfo = client.Market.Market_symbolInfo(symbol="BTCUSDT").result()
btcusdInfoResults = btcusdInfo[0].get('result')
markPrice = btcusdInfoResults[0].get('mark_price')
print(markPrice)

price_of_buys = []
price_of_sells = []
for i in range(1,50):
    price_of_buys.append(float(markPrice) - float(100*i))
    price_of_sells.append(float(markPrice) + float(100*i))
print(price_of_buys)
print(price_of_sells)

for orderPrice in price_of_buys:
    client.LinearOrder.LinearOrder_new(side="Buy",symbol="BTCUSDT",order_type="Limit",qty=0.1,price=orderPrice,time_in_force="GoodTillCancel",reduce_only=False, close_on_trigger=False).result()
for orderPrice in price_of_sells:
    client.LinearOrder.LinearOrder_new(side="Sell",symbol="BTCUSDT",order_type="Limit",qty=0.1,price=orderPrice,time_in_force="GoodTillCancel",reduce_only=False, close_on_trigger=False).result()
"""








orderbookCommand = client.Market.Market_orderbookL2_200(symbol="BTCUSD").result()
orderbook = orderbookCommand[0].get('result') # it returns a tuple of a dictionary, only 'results' contain data




threeMillionPrice = 0
totalBuys = 0
for i in range(len(orderbook)):
    if orderbook[i].get('side') == 'Buy':
        totalBuys += orderbook[i].get('size')
        if totalBuys > 3000000:
            threeMillionPrice = orderbook[i].get('price')
            break
print(totalBuys, threeMillionPrice)



threeMillionSell = 0
totalSells = 0
for i in range(len(orderbook)):
    if orderbook[i].get('side') == 'Sell':
        totalSells += orderbook[i].get('size')
        if totalSells > 3000000:
            threeMillionSell = orderbook[i].get('price')
            break
print(totalSells, threeMillionSell)
"""

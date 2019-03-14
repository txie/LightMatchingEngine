from lightmatchingengine.lightmatchingengine import LightMatchingEngine, Side
import json

lme = LightMatchingEngine()
buy_order, trades = lme.add_order("EUR/USD", 1.10, 1000, Side.BUY)
print ('{}'.format(buy_order.json()))
print ('order: {}'.format(buy_order))
print ('trade: {}'.format(trades))

print ('bids: {}'.format(type(lme.order_books['EUR/USD'].bids)))
eurusdBids = lme.order_books['EUR/USD'].bids
print(lme.order_books['EUR/USD'].json('bid'))
for bid in eurusdBids:
    for order in eurusdBids[bid]:
        print ('\t{} {}'.format(bid, order.json()))

print ('lme: {}'.format(lme.order_books))

sell_order, trades = lme.add_order("EUR/USD", 1.10, 1000, Side.SELL)
print (sell_order)
print (trades)

from lightmatchingengine.lightmatchingengine import LightMatchingEngine, Side

lme = LightMatchingEngine()
buy_order, trades = lme.add_order("EUR/USD", 1.10, 1000, Side.BUY)
print ('order: {}'.format(buy_order))
print ('trade: {}'.format(trades))

print ('lme: {}'.format(lme.order_books))

sell_order, trades = lme.add_order("EUR/USD", 1.10, 1000, Side.SELL)
print (sell_order)
print (trades)

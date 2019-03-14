#!flask/bin/python
from flask import Flask, request, jsonify
import json
from lightmatchingengine.lightmatchingengine import LightMatchingEngine, Side

app = Flask(__name__)
lme = LightMatchingEngine()

@app.route('/')
def index():
    return 'Light Matching Machine REST Demo'

@app.route('/order', methods=['POST'])
def submitOrder():
    content = request.get_json()
    print(content)
    instrument = content['instrument']
    price = content['price']
    quantity = content['quantity']
    side = Side.BUY if content['side'] == 'buy' else Side.SELL
    order, trades = lme.add_order(instrument, price, quantity, side)
    return_result = {'status': 'success', 'order-id': order.order_id}

    return jsonify(return_result)

@app.route('/order/<string:order_book>/<int:order_id>', methods=['GET'])
def lookupOrder(order_book, order_id):
    converted_trade_pair = order_book.replace('-', '/')
    print ('/order/<order_id> {}'.format(lme.order_books))
    orderbook = lme.order_books[converted_trade_pair]
    if orderbook == None:
        return jsonify({'status': 'error', 'message': 'trading pair {} not found'.format(converted_trade_pair)})
    else:
        order = orderbook.order_id_map[order_id]

        if order == None:
            return jsonify({'status': 'error', 'message': 'order {} not found'.format(order_id)})
        return json.dumps(order.__dict__)

@app.route('/orderbook/<string:symbol>/<string:side>', methods=['GET'])
def lookupOrderbook(symbol, side):
    converted_trade_pair = symbol.replace('-', '/')
    side = side.lower()
    orderbook = lme.order_books[converted_trade_pair]
    if orderbook == None:
        return jsonify({'status': 'error', 'message': 'trading pair {} not found'.format(converted_trade_pair)})
    else:
        orders = []
        if side == 'buy' or side == 'bid':
            for bidOrder in orderbook.bids:
                orders.append(bidOrder)       
        elif side == 'sell' or side == 'ask':     
            for askOrder in orderbook.asks:
                orders.append(askOrder)

        return json.dumps(orders)

if __name__ == '__main__':
    app.run(debug=True)

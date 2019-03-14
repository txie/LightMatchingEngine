import requests
import json

url = 'http://localhost:5000/order'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

payload = {"instrument": "EUR/USD", "price": 1.10, "quantity": 100, "side":"buy"}
for price in [1.10, 1.20, 1.30, 1.40]:
    payload['price'] = price
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print ('result: {}'.format(r))

btcPayload = {"instrument": "BTC/USDT", "price": 3800, "quantity": 1, "side":"buy"}
for price in [3800, 3900, 4000, 5000]:
    btcPayload['price'] = price
    r = requests.post(url, data=json.dumps(btcPayload), headers=headers)
    print ('result: {}'.format(r))
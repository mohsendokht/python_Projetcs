"""Gets coin price. 
"""


import requests

COIN_ID = 'bitcoin'
CURRENCY = 'usd'

url = f"https://api.coingecko.com/api/v3/simple/price?ids={COIN_ID}&vs_currencies={CURRENCY}"
data = requests.get(url, timeout=60).json()

coin_price = data[COIN_ID][CURRENCY]
print(coin_price)

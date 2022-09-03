from time import sleep
import requests

def BTCPrice():
    while True:
        try:
            url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDC'
            req = requests.get(url).json()['price']
            sleep(1)
            break
        except:
            sleep(10)
            continue 


    return req


from binance.client import Client
from binance.enums import *
from Secret import api_key, api_secret
from ValorAtivos import ValorBTC, ValorUSDC
from BTCPrice import BTCPrice
from time import sleep
import ccxt



def SellBTC(btc):
    client = Client(api_key, api_secret)
    ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})

    c = 0
    while True:
        value = btc - c
        try:
            order = client.create_order(
                symbol='BTCUSDC',
                side=SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=float(round(value, 5)),
            )
            break
        except:
            c += 0.00001
            continue

def BuyBTC(cash):

    client = Client(api_key, api_secret)
    ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})
    c = 0
    while True:
        value = (cash/float(BTCPrice())) - c
        try:
            order = client.create_order(
                symbol='BTCUSDC',
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=float(round(value, 5)),
            )
            break
        except:
            c += 0.00001
            continue


# V_BTC = ValorBTC()
# print(V_BTC)
# SellBTC(V_BTC)

# V_USDC = ValorUSDC()
# print(V_USDC)
# BuyBTC(V_USDC)
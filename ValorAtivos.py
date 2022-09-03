from binance.client import Client
from Secret import api_key, api_secret
from time import sleep



def ValorUSDC():
    while True:
        try:
            client = Client(api_key, api_secret).get_account()
            sleep(0.2)
            break
        except:
            continue

    lista_de_ativos = client['balances']

    for item in lista_de_ativos:
        if (item['asset'] == 'USDC'):
            ValorUSDT = (item['free'])

    return float(ValorUSDT)

def ValorBTC():

    while True:
        try:
            client = Client(api_key, api_secret).get_account()
            sleep(0.2)
            break
        except:
            continue

    lista_de_ativos = client['balances']

    for item in lista_de_ativos:
        if (item['asset'] == 'BTC'):
            ValorBTC = (item['free'])

    return float(ValorBTC)

from binance.client import Client
from Secret import api_key, api_secret

info = Client(api_key, api_secret).get_account()

lista_de_ativos = info['balances']

for item in lista_de_ativos:
    if( float(item['free']) > 0):
        print(f'{item["asset"]} -> {item["free"]}')
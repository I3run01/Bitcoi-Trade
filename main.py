from time import sleep
from BTCPrice import BTCPrice
from ValorAtivos import ValorBTC
from ValorAtivos import ValorUSDC
from Buy_Sell import SellBTC
from Buy_Sell import BuyBTC

print('Runing')
while True:

    sleep(0.5)

    saldo_USDC = ValorUSDC()
    saldo_BTC = ValorBTC()

    BTC_Price = float(BTCPrice())

    Base_BTC_Price = float(29200)
    Top_BTC_Price = float(30000)
    Over_BTC_Price = float(33000)

    if(BTC_Price >= Top_BTC_Price and BTC_Price <= Over_BTC_Price):
        #You should sell BTC -> USDC

        if(saldo_BTC > 0.0035):
            SellBTC(saldo_BTC)
            print(f'I sold BTC for {BTC_Price}')
            
        else:
            continue


    elif(BTC_Price <= Base_BTC_Price):
        #You should buy BTC

        if (saldo_USDC > 20):
            BuyBTC(saldo_USDC)
            print(f'I bought BTC for {BTC_Price}')
            
        else:
            continue

    elif(BTC_Price > Over_BTC_Price):
        #You should buy BTC and finish the bot

        if (saldo_USDC > 20):
            BuyBTC(saldo_USDC)
            print(f'I bought BTC for {BTC_Price}')
            break

        else:
            break
    else:
        #Do nothing
        sleep(0.5)
    
    




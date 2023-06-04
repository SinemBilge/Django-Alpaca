import alpaca_trade_api as api 
from django.shortcuts import render

ALPACA_API_KEY= "PKWLEWOIBWF0BUIAG309"
ALPACA_SECRET_KEY = "rgxjmZlnTSpDLg99BPH5DASMXrwIOuNPglO0n92h"
BASE_URL= "https://paper-api.alpaca.markets"

# Instantiate REST API Connection
alpaca = api.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=BASE_URL, api_version='v2')
def Alaccount():
	return alpaca.get_account()

#requesting daily data of Apple Stock for the last 100 days.
#APPLE_DATA = api.get_barset('AAPL', 'day', limit=100)

# Preview Datas
#print(APPLE_DATA.df.head())

#look at the status of your portfolio.
#aapl_position = api.get_position('AAPL')



def alpaccount():
# Get a list of all of our positions.
    portfolio = alpaca.list_positions()
    data = []
    for position in portfolio:
        data.append({'qty':position.qty,'symbol':position.symbol})
    return data
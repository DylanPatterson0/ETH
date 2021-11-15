from dydx3 import Client
from dydx3.constants import API_HOST_ROPSTEN
from dydx3.constants import NETWORK_ID_ROPSTEN
from dydx3.constants import MARKET_ETH_USD
from web3 import Web3

# Ganache test address
ETHEREUM_ADDRESS = '0xb0b6dC5d8b4cd9e223711CaDc8C2e2E09EAd12c1'

# Ganache node
WEB_PROVIDER_URL = 'HTTP://127.0.0.1:7545'

client = Client(
    network_id=NETWORK_ID_ROPSTEN,
    host=API_HOST_ROPSTEN,
    default_ethereum_address=ETHEREUM_ADDRESS,
    web3=Web3(Web3.HTTPProvider(WEB_PROVIDER_URL)),
)

market_eth = MARKET_ETH_USD


def market_client(market):

    market_client = client.public.get_markets(market=market)

    return market_client


def print_market_data(market_obj=market_eth):

    market_data = market_client(market_obj)

    index_price = market_data['markets']['ETH-USD']['indexPrice']
    price_change = market_data['markets']['ETH-USD']['priceChange24H']
    volume = market_data['markets']['ETH-USD']['volume24H']

    percent_change = round((float(price_change)/float(index_price)*100), 2)



    ret_val = ("Current Index Price: " + str(index_price))
    ret_val += ("\nPrice Change in 24H: " + str(percent_change) + "%")
    ret_val += ("\nVolume in 24H: " + str(volume))

    return ret_val


# returns market data in dictionary structure
def get_market_data(market_obj=market_eth):

    market_data = market_client(market_obj)

    index_price = market_data['markets']['ETH-USD']['indexPrice']
    price_change = market_data['markets']['ETH-USD']['priceChange24H']
    volume = market_data['markets']['ETH-USD']['volume24H']

    percent_change = round((float(price_change)/float(index_price)*100), 2)

    ret_val = {'Index': index_price,
               '%Change': percent_change,
               'Volume': volume}

    return ret_val


print(print_market_data())












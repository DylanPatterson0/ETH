"""

This program utilized the dYdX API to retrieve live data for the ETH/USD market.

The data retrieved and printed to the user includeds the current ETH/USD exchange rate,
the % change in the exchange rate in the last 24H, as well as the total volume traded
in the last 24H.

This program will later be expanded to show how the dYdX API can handle trades using the
Ropsten test network. This program also relies on an ETH address from a local Ganache node.

for more information on the dYdX API visit:
https://docs.dydx.exchange/#general

"""


from dydx3 import Client
from dydx3.constants import API_HOST_ROPSTEN
from dydx3.constants import NETWORK_ID_ROPSTEN
from dydx3.constants import MARKET_ETH_USD
from web3 import Web3

# Ganache test address
ETHEREUM_ADDRESS = '0x483CcF01D4eb95B0ee1d58b2b3CeDc4f73b057dF'

# Ganache node
WEB_PROVIDER_URL = 'HTTP://127.0.0.1:7545'

# create client node
client = Client(
    network_id=NETWORK_ID_ROPSTEN,
    host=API_HOST_ROPSTEN,
    default_ethereum_address=ETHEREUM_ADDRESS,
    web3=Web3(Web3.HTTPProvider(WEB_PROVIDER_URL)),
)

market_eth = MARKET_ETH_USD


# fetch ETH/USD market data from API client
def market_client(market):

    data = client.public.get_markets(market=market)

    return data


# returns market data in dictionary structure
def parse_data(market_obj=market_eth):

    market_data = market_client(market_obj)

    index_price = market_data['markets']['ETH-USD']['indexPrice']
    price_change = market_data['markets']['ETH-USD']['priceChange24H']
    volume = market_data['markets']['ETH-USD']['volume24H']

    percent_change = round((float(price_change)/float(index_price)*100), 2)

    ret_val = {'Index': index_price,
               '%Change': percent_change,
               'Volume': volume}

    return ret_val


# function to parse data and print relevant metrics
def print_market_data(market_obj=market_eth):

    data = parse_data()

    ret_val = ("Current Index Price: " + str(data['Index']))
    ret_val += ("\nPrice Change in 24H: " + str(data['%Change']) + "%")
    ret_val += ("\nVolume in 24H: " + str(data['Volume']))

    print(ret_val)


print_market_data()












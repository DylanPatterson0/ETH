from web3 import Web3
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

# use Infura to get local node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/a520cf83bf5f4326b230d15ffd572a44'))

# test update

def get_total_burned():

    latest_block = w3.eth.getBlock('latest').number

    total_burned = 0

    for i in range(latest_block-50, latest_block):

        # get gas and base fee (in hex) from latest block
        gas_used = w3.eth.getBlock(i).gasUsed
        base_fee = w3.eth.getBlock(i).baseFeePerGas

        # convert hex to decimal, then convert to WEI
        base_fee = base_fee/10**9

        # ETH burned in block: gas * base fee, convert to ETH, round to 4 decimal places
        burned = round(((gas_used * base_fee)/10**9), 4)

        total_burned += burned
        total_burned = round(total_burned, 4)

    return total_burned


def get_price():

    price_response = cg.get_price(ids='ethereum', vs_currencies='usd')

    price = price_response['ethereum']['usd']

    return price


def print_burned():

    burned = get_total_burned()

    price = get_price()

    dollars_burned = round(burned*price, 2)

    formatted_dollars_burned = "$ {:,.2f}".format(dollars_burned)

    print(formatted_dollars_burned, "were burned in the past 50 blocks")





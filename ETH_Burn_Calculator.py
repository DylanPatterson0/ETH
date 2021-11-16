"""

Program built to show the effect of EIP-1559, or the London Hard Fork

For each ETH block, there is a set 'base fee per gas' which is used to calculate
the gas fees transactors will pay to the network to have their transaction included
in the next block.

This base fee is multiplied by the total gas used in the mining of the block to
calculate the total transaction fee. As of the London Hard Fork, around August of 2020,
these transaction fees are burned, and thus the value of the burned tokens are
re-distributed to the entire network.

This program utilizes the Web3 API to retrieve live ETH blockchain data as well as the
CoinGecko API to retrieve the live ETH/USD price data. The program then uses this live data to
calculate the USD amount of ETH burned in the last 'n' blocks.

"""


from web3 import Web3
from pycoingecko import CoinGeckoAPI

# use Infura to get local node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/a520cf83bf5f4326b230d15ffd572a44'))


# function to grab the total ETH burned in the last 'n' blocks, default 50
def get_total_burned(n=50):

    # fetch latest block number
    latest_block = w3.eth.getBlock('latest').number

    # initialize counter at 0, keeps track of total ETH burned through the for loop
    total_burned = 0

    # iterate from starting block to latest block
    for i in range(latest_block-n, latest_block):

        # get gas used and base fee from latest block
        gas_used = w3.eth.getBlock(i).gasUsed
        base_fee = w3.eth.getBlock(i).baseFeePerGas

        # convert to WEI
        base_fee = base_fee/10**9

        # ETH burned in block: gas * base fee, convert from WEI to ETH, round to 4 decimal places
        burned = round(((gas_used * base_fee)/10**9), 4)

        # update total counter
        total_burned += burned

    # round total
    total_burned = round(total_burned, 4)

    # return type float
    return total_burned


# function to connect to CoinGecko API and fetch latest ETH/USD price
def get_price():

    # create API object to fetch data
    cg = CoinGeckoAPI()

    # returns AttributeDict with ETH/USD price data
    price_response = cg.get_price(ids='ethereum', vs_currencies='usd')

    # parse data to return int price of ETH/USD
    price = price_response['ethereum']['usd']

    # return type float
    return price


# void function to print out message with USD burned in last n blocks, default 50
def print_burned(n=50):

    # call other functions in file
    burned = get_total_burned()
    price = get_price()

    # multiply burned and price to get total USD burned
    dollars_burned = round(burned*price, 2)

    # change format from decimal to $
    formatted_dollars_burned = "$ {:,.2f}".format(dollars_burned)

    # print message
    print(formatted_dollars_burned, "were burned in the past", n, "blocks")


print_burned()



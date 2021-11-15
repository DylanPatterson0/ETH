from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

dict = cg.get_price(ids='ethereum', vs_currencies='usd')

print(dict)

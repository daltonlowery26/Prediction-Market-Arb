# packages and env data
from dotenv import load_dotenv
import os
from py_clob_client.client import ClobClient
import pandas as pd

# set cd
load_dotenv()
os.chdir("C:/Users/dalto/OneDrive/Pictures/Documents/Projects/Pred Market Arb/")


# host, key, chainid
host = "https://clob.polymarket.com"
key = os.getenv("PK")
chain_id = 137  # Polygon Mainnet chain ID

# intialize client
client = ClobClient(host, key=key, chain_id=chain_id)

# get markets
resp = client.get_simplified_markets(next_cursor="")
df = pd.DataFrame(resp)
df.to_csv("polymarket_data/sample_markets.csv")


print("done")



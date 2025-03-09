import requests
import pandas as pd
import os

os.chdir("C:/Users/dalto/OneDrive/Pictures/Documents/Projects/Pred Market Arb/")
url = "https://api.elections.kalshi.com/trade-api/v2/markets" # market source

# params and header
headers = {"accept": "application/json"}
params = {"limit": 200, "status": "open"}

# pull data
response = requests.get(url, headers=headers, params=params).json() # pull response and convert to json

# export as df
df = pd.DataFrame(response)
df.to_csv('kalshi_data/raw/markets_data.csv')
print("Done!")
# packages and env data
from dotenv import load_dotenv
import os
from py_clob_client.client import ClobClient
import pandas as pd
import requests

# set cd
load_dotenv()
os.chdir("C:/Users/dalto/OneDrive/Pictures/Documents/Projects/Pred Market Arb/")

# https://docs.polymarket.com/#query-parameters-2
host = "https://gamma-api.polymarket.com"

# Function to make API calls
def get_markets(endpoint, params=None):
    url = f"{host}{endpoint}"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Example calls
market_data = get_markets("/markets?start_date_min=2025-02-01T00:00:00Z&limit=500&closed=false")  # get market starting after feb first that are still active, limit 500

# Convert to DataFrame
df = pd.DataFrame(market_data)

# Export to CSV
df.to_csv("polymarket_data/data/market_data.csv", index=False)

print("Data exported to market_data.csv")

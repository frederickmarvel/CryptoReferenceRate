import os
import requests
from dotenv import load_dotenv
import pandas as pd 
import numpy as np 
from datetime import time
import asyncio
from datetime import datetime

load_dotenv()
idx_api_key = os.getenv("idx_api_key")
idx_secret_key = os.getenv("idx_secret_key")
print(idx_secret_key)

url_last_price = "https://indodax.com/api/ticker/btcidr"
async def requests_get(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

requests_get(url_last_price)
requests_get(url_last_price)
requests_get(url_last_price)
requests_get(url_last_price)
requests_get(url_last_price)
requests_get(url_last_price)
requests_get(url_last_price)

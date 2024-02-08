import os
import requests
import pandas as pd 
import numpy as np

def requests_get(url):
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
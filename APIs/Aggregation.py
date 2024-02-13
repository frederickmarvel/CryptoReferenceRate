import pandas as pd
import numpy as np 
import APIs.Indodax as idx 
import pymysql as mysql
import requests
from datetime import datetime

# Connect to MySQL database
db = mysql.connect(
    host="localhost",
    user="admin",
    password="M4rv3lnur$17",
    database="crypto_reference_rate"
)
cursor = db.cursor()


def insert_idx_data():
    data = idx.get_data("btcidr")
    lastPrice = data['ticker']['last']
    volumeTrade= data['ticker']['vol_btc']
    server_time = datetime.now()
    source = "indodax"
    query = ("INSERT INTO btc_idr_price (last_price, volume, server_time, source)"
             "VALUES (%s, %s, %s, %s)")
    data = (lastPrice, volumeTrade, server_time, source)
    cursor.execute(query, data)
    db.commit()

# insert_idx_data()


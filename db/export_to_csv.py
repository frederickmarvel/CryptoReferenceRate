import pymysql
import pandas as pd

db_connection = pymysql.connect(
    host="localhost",
    user="admin",
    passwd="M4rv3lnur$17",
    database="crypto_reference_rate"
)


query = "SELECT * FROM btc_idr_price"
df = pd.read_sql_query(query, db_connection)
df.to_csv('output_file.csv', index=False)
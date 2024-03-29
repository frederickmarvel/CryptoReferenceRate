import pymysql

db_connection = pymysql.connect(
    host="localhost",
    user="admin",
    passwd="M4rv3lnur$17",
    database="crypto_reference_rate"
)


cursor = db_connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS btc_idr_price (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_price DECIMAL(16, 2),
    volume DECIMAL(16, 2),
    server_time VARCHAR(255),
    source VARCHAR(255)
)
""")

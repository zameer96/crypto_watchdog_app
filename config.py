import os
from urllib.parse import quote_plus

class Config:
    # DB_HOST = os.environ.get('DATABASE_HOST')
    # DB_USER = os.environ.get('DATABASE_USER')
    # DB_PASSWORD = os.environ.get('DATABASE_PASSWORD')
    # DB_NAME = os.environ.get('DATABASE_NAME')

    DB_HOST = "cwddatabase.mysql.database.azure.com"
    DB_USER = "cryptowddbusername"
    DB_PASSWORD = "Ethereum@2024#$"
    DB_NAME = "crypto_watchdog"
    DB_PORT = "3306"

    encoded_password = quote_plus(DB_PASSWORD)

    # Construct the database URI using the separate configuration variables
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class CryptoConfig:
    CRYPTO_LIST = {
        "btc": "bitcoin",
        "eth": "ethereum",
        "xrp": "ripple",
        "doge": "dogecoin"
    }
import pymongo 
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
DB_CONN_URL = os.getenv('DB_CONN_URL')

print(DB_CONN_URL)
client = pymongo.MongoClient(DB_CONN_URL)

db = client["xpense_db"]
transaction_collection = db["xpense_collection"]
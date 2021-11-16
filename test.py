import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
tb = db["USER"]
x = tb.insert_one({
    "account": "admin",
    "password": "admin123",
})

print(x.inserted_id)
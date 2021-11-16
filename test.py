import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
users = db["USER"]
result = users.find_one({"account": "admin"})
id = result["_id"]
print(str(id))
# print(new ObjectId().str)
# print(type(id))

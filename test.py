import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
known_words = db["KNOWN_WORDS"]
known_words.update_one(
	{"user_id": "61944ed2999c486394b9f3ea"},
	{"$addToSet": {"words": {"$each": ["to","the"]}}}
)

known_words.update_one(
	{"user_id": "61944ed2999c486394b9f3ea"},
	{"$set": {"words": []}},
)
# print(new ObjectId().str)
# print(type(id))

import pymongo
from config import MONGO_URL, MONGO_DB

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

# 查询
def db_query(db_name: str, cond: dict, find_one: bool = False):
	

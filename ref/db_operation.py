import pymongo
from config import MONGO_URL, MONGO_DB

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

# 处理查询结果
def to_list_or_dict(cursor):
    new_list = list(cursor)
    count = len(new_list)
    if(count == 1):
        return new_list[0]
    else:
        return {
            "count": count,
            "data": new_list
        }

# 查询
def db_query(
    db_name: str, #表名
    cond: dict = None, #条件
    keys: dict = None, #筛选字段，返回值为1
    size: int = 10, #每页条数
    no: int = 0, #页数
    find_one: bool = False):
    collection = db[db_name]
    if(find_one):
        query_result = collection.find_one(cond, keys)
    else:
        start = size*no
        query_result = to_list_or_dict(collection.find(cond, keys).limit(size).skip(start))
    return query_result
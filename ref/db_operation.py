import pymongo
from config import MONGO_URL, MONGO_DB

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

# 将查询结果转为列表或字典
def to_list_or_dict(cursor):
    new_list = list(cursor)
    count = len(new_list)
    if(count == 0):
        return None
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
    ):
    collection = db[db_name]
    result = collection.find(cond, keys).limit(size).skip(size*no)
    query_result = to_list_or_dict(result)
    return query_result

# 插入
def db_insert(
        db_name: str,
        documents,
        only_one: bool = False
    ):
    collection = db[db_name]
    if(only_one):
        new_id = collection.insert_one(documents)
    else:
        new_id = collection.insert_one(documents)
    return new_id
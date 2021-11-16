from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
import pymongo
from config import *

# client = pymongo.MongoClient(MONGO_URL)
# db = client[MONGO_DB]
# tb = db["knownWords"]
# x = tb.insert_one({
#     "the": 1
# })

app = FastAPI()

# map = Code("function() { for (var key in this) { emit(key, null); } }")
# reduce = Code("function(key, stuff) { return null; }")
# known_words = db["knownWords"].map_reduce(map, reduce, "myresults").distinct('_id')

# print(known_words)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    context: str

def getUUID():
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    return suid


@app.get("/")
async def main():
    return {"message": "Hello , this is FastAPI."}

@app.post("/wordfrequency/")
async def cal_word_frequency(body: Item):
    context = body.context.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~0123456789':
        context = context.replace(ch, " ")
    words  = context.split()
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        if word in known_words:
            continue
        counts[word] = counts.get(word,0) + 1
    # 返回无序的对象数组
    items = []
    for key in counts.keys():
        items.append({
            "id": getUUID(),
            "word": key,
            "frequency": counts[key]
        })
    # 返回排序好的二维数组
    # items = list(counts.items())
    # items.sort(key=lambda x:x[1], reverse=True)
    return items

@app.post("/add_known_word/{word}")
async def add_known_word(word: str):
    known_words.add(word)
    return {
        "msg": "添加熟词成功！"
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# class User(BaseModel):
#     account: str
#     password: str

# # 添加用户
# @app.post("/user/register")
# async def register(arg: register):
#     tb = db["USER"]
#     x = tb.insert_one({
#         "account": arg.account,
#         "password": arg.password,
#     })
#     return x.inserted_id

# # 删除用户
# @app.delete("/user/{user_id}")
# async def delete_user(arg: register):
#     tb = db["USER"]
#     x = tb.insert_one({
#         "account": arg.account,
#         "password": arg.password,
#     })
#     return x.inserted_id

# # 更新用户
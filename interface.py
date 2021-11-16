from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    account: str
    password: str

# 用户注册
@app.post("/user/register")
async def register(arg: User):
    users = db["USER"]
    if(users.find_one({"account": arg.account}) == None):
        result = users.insert_one({
            "account": arg.account,
            "password": arg.password,
        })
        known_words = db["KNOWN_WORDS"]
        known_words.insert_one({
            "user_id": str(result.inserted_id),
            "words": [],
        })
        return {
            "data": str(result.inserted_id)
        }
    return {
        "msg": "账户名称重复"
    }

# 用户登录
@app.post("/user/login")
async def login(arg: User):
    users = db["USER"]
    result = users.find_one({"account": arg.account})
    if(result == None):
        return {
            "msg": "账户不存在"
        }
    elif(result["password"] != arg.password):
        return {
            "msg": "密码错误"
        }
    return {
        "data": str(result["_id"])
    }     

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






# class Item(BaseModel):
#     context: str

# def getUUID():
#     uid = str(uuid.uuid4())
#     suid = ''.join(uid.split('-'))
#     return suid


# @app.get("/")
# async def main():
#     return {"message": "Hello , this is FastAPI."}

# @app.post("/wordfrequency/")
# async def cal_word_frequency(body: Item):
#     context = body.context.lower()
#     for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~0123456789':
#         context = context.replace(ch, " ")
#     words  = context.split()
#     counts = {}
#     for word in words:
#         if len(word) == 1:
#             continue
#         if word in known_words:
#             continue
#         counts[word] = counts.get(word,0) + 1
#     # 返回无序的对象数组
#     items = []
#     for key in counts.keys():
#         items.append({
#             "id": getUUID(),
#             "word": key,
#             "frequency": counts[key]
#         })
#     # 返回排序好的二维数组
#     # items = list(counts.items())
#     # items.sort(key=lambda x:x[1], reverse=True)
#     return items

# @app.post("/add_known_word/{word}")
# async def add_known_word(word: str):
#     known_words.add(word)
#     return {
#         "msg": "添加熟词成功！"
#     }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


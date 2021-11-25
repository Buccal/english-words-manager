from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

class Source(BaseModel):
    user_id: str
    context: str

# 计算词频
@app.post("/wordfrequency")
async def cal_word_frequency(source: Source):
    known_words = db["KNOWN_WORDS"]
    context = source.context.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~0123456789“”':
        context = context.replace(ch, " ")
    words  = context.split()
    counts = {}
    result = known_words.find_one({"user_id": source.user_id})
    if(result == None):
        return {
            "msg": "用户不存在"
        }
    exclude = result["words"]
    for word in words:
        if len(word) == 1:
            continue
        if word in exclude:
            continue
        counts[word] = counts.get(word,0) + 1
    # 返回无序的对象数组
    items = []
    for key in counts.keys():
        items.append({
            "word": key,
            "frequency": counts[key]
        })
    # 返回排序好的二维数组
    # items = list(counts.items())
    # items.sort(key=lambda x:x[1], reverse=True)
    return {
        "data": items
    }

class Words(BaseModel):
    user_id: str
    words: list

# 批量添加熟词
@app.post("/known_word/add")
async def add_known_word(data: Words):
    known_words = db["KNOWN_WORDS"]
    result = known_words.find_one({"user_id": data.user_id})
    if(result == None):
        return {
            "msg": "用户不存在"
        }
    known_words.update_one(
        {"user_id": data.user_id},
        {"$addToSet": {"words": {"$each": data.words}}}
    )
    return {
        "msg": "添加熟词成功！"
    }

# 获取熟词
@app.get("/known_word/list/{user_id}")
async def get_known_words(user_id: str):
    known_words = db["KNOWN_WORDS"]
    result = known_words.find_one({"user_id": user_id})
    if(result == None):
        return {
            "msg": "用户不存在"
        }
    return {
        "data": result["words"]
    }

# 获取模板词库
@app.get("/template_word/list/{level}")
async def get_known_words(level: str):
    template_words = db["TEMPLATE_WORDS"]
    result = template_words.find_one({"level": level})
    if(result == None):
        return {
            "msg": "用户不存在"
        }
    return {
        "data": result["words"]
    }

# @app.get("/")
# async def main():
#     return {"message": "Hello , this is FastAPI."}





if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


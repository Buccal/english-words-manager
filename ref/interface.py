from fastapi import FastAPI
from typing import Optional
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymongo
from config import MONGO_URL, MONGO_DB

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
        template_words = db["TEMPLATE_WORDS"]
        user_words = db["USER_WORDS"]
        user_words.insert_one({
            "user_id": str(result.inserted_id),
            "words": list(template_words.find({}, { '_id': 0 })),
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
    context: Optional[str] = None

# 计算词频
@app.post("/wordfrequency")
async def cal_word_frequency(source: Source):
    user_words = db["USER_WORDS"]
    context = source.context.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~0123456789“”':
        context = context.replace(ch, " ")
    words  = context.split()
    counts = {}
    if source.user_id == True:
        user_words = user_words.find_one({"user_id": source.user_id})
        result = [item['word'] for item in user_words.words]
        if(result == None):
            return {
                "msg": "用户不存在"
            }
        exclude = result["words"]
    else:
        exclude = []
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
@app.post("/user_words/set_known")
async def add_user_word(data: Words):
    user_words = db["USER_WORDS"]
    result = user_words.find_one({"user_id": data.user_id})
    if(result == None):
        return {
            "msg": "用户不存在"
        }
    for word in data.words:
        if(not user_words.find_one({"user_id": data.user_id, "words.word": word})):
            user_words.update(
                { "user_id": data.user_id },
                { "$push": { "words": { "word": word, "Group": word[0].upper(), "isKnown": True, "level": None } } },
                True
            )
        else:
            user_words.update(
                { "user_id": data.user_id, "words.word": word },
                { "$set": { "words.$.isKnown": True } }
            )
    return {
        "msg": "添加熟词成功！"
    }

# 获取熟词
@app.get("/user_words/known_list/{user_id}")
async def get_user_words(user_id: str):
    user_words = db["USER_WORDS"]
    user = user_words.find_one({"user_id": user_id})
    if(user == None):
        return {
            "msg": "用户不存在"
        }
    result = user_words.aggregate([
        { "$match": { "user_id": user_id, "words.isKnown": True }},
        { "$project": {
            "_id": 0,
            "words": {
                "$filter": {
                    "input": "$words",
                    "as": "words",
                    "cond": {
                        "$eq": ["$$words.isKnown", True]
                    }
                }
            }
        }
    }])
    tempRes = list(result)
    if(tempRes == None):
        return { "data": [] }
    return {
        "data": [item['word'] for item in tempRes[0]["words"]]
    }

# 获取模板词库
@app.get("/user_words/template_list/{user_id}/{level}")
async def get_user_words(user_id: str, level: str):
    user_words = db["USER_WORDS"]
    user = user_words.find_one({"user_id": user_id})
    if(user == None):
        return {
            "msg": "用户不存在"
        }
    result = user_words.aggregate([
        { "$match": { "user_id": user_id, "words.level": level }},
        { "$project": {
            "_id": 0,
            "words": {
                "$filter": {
                    "input": "$words",
                    "as": "words",
                    "cond": {
                        "$eq": ["$$words.level", level]
                    }
                }
            }
        }
    }])
    if(result == None):
        return { "data": [] }
    return {
        "data": list(result)[0]["words"]
    }

# @app.get("/")
# async def main():
#     return {"message": "Hello , this is FastAPI."}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("interface:app", host="127.0.0.1", port=8000, reload=True)


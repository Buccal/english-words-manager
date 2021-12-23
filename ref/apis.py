# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI, Request

# OAuth2PasswordRequestForm是一个类依赖项项，声明了如下的请求表单：username、password
from fastapi.security import OAuth2PasswordRequestForm
from model import Token, User, CustomException
from dependencies import authenticate_user, create_access_token, get_current_active_user, register_user
from config import USER_DB

from fastapi.responses import JSONResponse, Response
from response_info import status_code_list, default_msg_list

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 统一异常处理
@app.exception_handler(CustomException)
async def unicorn_exception_handler(request: Request, exc: CustomException = Depends()):
    return JSONResponse(
        status_code=status_code_list.get(exc.code, exc.code),
        content={
            'code': exc.code,
            'message': exc.msg if exc.msg != None else default_msg_list.get(exc.code, "未知错误"),
            'data': exc.data,
        }
    )

# 用户注册
@app.post("/user/register", response_description="注册新用户")
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    register_user(USER_DB, form_data.username, form_data.password)

# 获取令牌
@app.post("/user/login", response_description="获取令牌", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 获取并验证用户信息
    user = authenticate_user(USER_DB, form_data.username, form_data.password)

    # 创建访问令牌
    create_access_token(user.username)

# 查询用户本人的信息
@app.get("/user/info", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# 计算词频
@app.post("/wordsfrequency")
async def cal_words_frequency(context: str, current_user: User = Depends(get_current_active_user)):
    
    words = separate_words(context)


    user_words = db["USER_WORDS"]


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
    

    return {
        "data": items
    }


@app.get("/user/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("security:app", host="127.0.0.1", port=8000, reload=True)

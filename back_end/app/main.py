# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI, Request

# OAuth2PasswordRequestForm是一个类依赖项项，声明了如下的请求表单：username、password
from fastapi.security import OAuth2PasswordRequestForm
from model import Token, User, CustomException, Context, UserInfo
from dependencies import authenticate_user, create_access_token, get_current_active_user, register_user, separate_words, count_words
from config import USER_DB

from fastapi.responses import JSONResponse, Response
from response_info import status_code_list, default_msg_list

from fastapi.middleware.cors import CORSMiddleware
from db_operation import db_query

app = FastAPI()

origins = ["*"]

# 允许跨域
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
            'data': exc.data,
            'msg': exc.msg if exc.msg != None else default_msg_list.get(exc.code, "未知错误"),
        }
    )

# 用户注册
@app.post("/user/register", response_description="注册新用户")
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    return register_user(USER_DB, form_data.username, form_data.password)

# 用户登录
@app.post("/user/login", response_description="获取令牌", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 获取并验证用户信息
    user = authenticate_user(USER_DB, form_data.username, form_data.password)

    # 创建访问令牌
    create_access_token(user.username)

# 查询用户本人的信息
@app.get("/user/info", response_model=UserInfo)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return {
        "code": 200,
        "data": current_user,
        "msg": "ok"
    }

# 计算词频
@app.post("/wordFrequency")
async def cal_words_frequency(ctx: Context, current_user: User = Depends(get_current_active_user)):
    context = ctx.content
    words = separate_words(context)
    exclude = db_query("USER_WORDS", {"username": current_user.username}) or []
    frequencyList = count_words(words, exclude)
    raise CustomException(code=200, data=frequencyList)

# 测试
@app.get("/test")
async def test():
    raise CustomException(code=200)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI, Request

# OAuth2PasswordRequestForm是一个类依赖项项，声明了如下的请求表单：username、password
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware

from model import User, CustomException, Context, UserInfo
from dependencies import login_user, create_access_token, get_current_active_user, register_user, separate_words, count_words, get_user_template_words
from config import USER_DB, WORD_DB
from response_info import status_code_list, default_msg_list
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
@app.post("/user/register", response_description="新用户")
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    return register_user(USER_DB, form_data.username, form_data.password)

# 用户登录
@app.post("/user/login", response_description="获取令牌")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_user(USER_DB, form_data.username, form_data.password)

# 查询用户本人的信息
@app.get("/user/info", response_description="获取用户基本信息")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return CustomException(code=200, data=dict(current_user), msg="ok")

# 计算词频
@app.post("/wordFrequency", response_description="计算单词频率")
async def cal_words_frequency(ctx: Context, current_user: User = Depends(get_current_active_user)):
    context = ctx.content
    words = separate_words(context)
    exclude = current_user.words
    frequencyList = count_words(words, exclude)
    return CustomException(code=200, data=frequencyList)

# 获取模板单词
@app.get("/templateWords/{level}")
async def get_template_words(level: str, current_user: User = Depends(get_current_active_user)):
    return get_user_template_words(WORD_DB, level, current_user.words)

# 添加已熟知单词
@app.post("/user/addWord")
async def add_user_word(data: Words, current_user: User = Depends(get_current_active_user)):


# 测试
@app.get("/test")
async def test():
    raise CustomException(code=200)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


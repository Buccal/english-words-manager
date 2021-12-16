# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI

# OAuth2PasswordRequestForm是一个类依赖项项，声明了如下的请求表单：username、password
from fastapi.security import OAuth2PasswordRequestForm
from model import Token, User
from dependencies import authenticate_user, create_access_token, get_current_active_user, register_user
from raise_error import raise_error
from config import USER_DB

app = FastAPI()

# 用户注册
@app.post("/user/register", response_description="注册新用户", response_model=User)
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    return register_user(USER_DB, form_data.username, form_data.password)

# 获取令牌
@app.post("/token", response_description="获取令牌", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 获取并验证用户信息
    user = authenticate_user(USER_DB, form_data.username, form_data.password)

    # 创建访问令牌
    access_token = create_access_token(user.username)

    # 返回Bearer令牌：访问令牌的字符串、令牌类型
    return {"access_token": access_token, "token_type": "bearer"}

# 查询用户本人的信息
@app.get("/user/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/user/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("security:app", host="127.0.0.1", port=8000, reload=True)


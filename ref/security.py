# -*- coding: UTF-8 -*-
from fastapi import Depends, FastAPI

from fastapi.security import OAuth2PasswordRequestForm
from model import Token, User
from dependencies import authenticate_user, create_access_token, get_current_active_user
from raise_error import raise_error

app = FastAPI()

# 用户数据（模拟）


# 获取令牌
@app.post("/login", response_model=Token)
# OAuth2PasswordRequestForm是一个类依赖项项，声明了如下的请求表单：
# - username
# - password
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 获取并验证用户信息
    user = authenticate_user("User", form_data.username, form_data.password)
    if not user:
        raise_error(401, "用户名或密码错误")

    # 创建访问令牌
    access_token = create_access_token(user.username)

    # 返回Bearer令牌：访问令牌的字符串、令牌类型
    return {"access_token": access_token, "token_type": "bearer"}

# 查询用户本人的信息
@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("security:app", host="127.0.0.1", port=8000, reload=True)


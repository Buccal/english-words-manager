# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

# OAuth2：一个规范，它定义了几种处理身份认证和授权的方法
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# passlib：处理哈希加密的包
from passlib.context import CryptContext

# JWT：JSON Web Tokens
from jose import JWTError, jwt

# 生成随机秘钥命令：openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"# 密钥
ALGORITHM = "HS256" # 哈希算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 访问令牌过期分钟

# 用户数据（模拟）
fake_users_db = {
    "alice": {
        "username": "alice",
        "email": "alice@example.com",
        "hashed_password": "$2b$12$MP0NyRYuGkOFTrVBBtuH4O63cAEz8OPtsNCcjwB9eFn0YCzyMjJ6K",
        "disabled": False,
    }
}


# 令牌空壳
class Token(BaseModel):
    access_token: str
    token_type: str

# 令牌数据
class TokenData(BaseModel):
    username: Optional[str] = None

# 用户基础模型
class User(BaseModel):
    username: str
    email: Optional[str] = None
    disabled: Optional[bool] = None

# 用户输入数据模型
class UserInDB(User):
    hashed_password: str

# 创建PassLib上下文：CryptContext(schemes-加密方案（bcrypt-加密算法）; deprecated-废弃)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme-令牌对象; token: str = Depends(oauth2_scheme)后就是之前加密的令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


app = FastAPI()


# 验证密码: plain_password-普通密码; hashed_password-哈希密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 获取密码哈希
def get_password_hash(password):
    # 将JSON对象编码为密集且没有空格的长字符串，相同密码可以转成不同的字符串，但验证都能通过
    return pwd_context.hash(password)

# 获取用户
def get_user(db, username: str):
    # 判断用户是否存在
    if username in db:
        user_dict = db[username]
        # 创建用户模型
        return UserInDB(**user_dict) # *表示元组，**表示字典

# 验证用户，成功返回用户信息
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    # 如果用户不存在或者密码错误
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user # <class '__main__.UserInDB'>

# 创建访问令牌
def create_access_token(*, data: dict, expires_delta:  Optional[timedelta] = timedelta(minutes=15)):
    to_encode = data.copy()
    # expire-令牌到期时间 
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire}) # {'sub': 用户名, 'exp': datetime.datetime类型时间}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 获取当前用户
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # token加密
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# 获取当前激活用户
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# 获取令牌
@app.post("/token", response_model=Token)
# OAuth2PasswordRequestForm是一个类依赖项项，声明了如下的请求表单：
# - username
# - password
# - grant_type：可选
# - scope：可选，是一个由空格分隔的字符串组成的大字符串
# - client_id：可选
# - client_secret：可选
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # 获取并验证用户信息
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            # 规范要求
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 设置令牌过期时间
    # timedelta表示两个datetime对象之间的差异。（来自datetime包）
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # 0:30:00

    # 创建访问令牌
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

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


# OAuth2：一个规范，它定义了几种处理身份认证和授权的方法
from fastapi.security import OAuth2PasswordBearer

# passlib：处理哈希加密的包
from passlib.context import CryptContext

# JWT：JSON Web Tokens
from jose import JWTError, jwt

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status

from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends

from model import TokenData, UserInDB, User
from decrypt_data import decrypt_data
from raise_error import raise_error
from db_operation import db_query, db_insert
from config import USER_DB

# 生成随机秘钥命令：openssl rand -hex 32
SECRET_KEY = "9fb2c88349f6ecaf46fd904495a93d132eca5d8c4747ca6ea31910507ed0e8bc"# 密钥
ALGORITHM = "HS256" # 哈希算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 默认访问令牌过期时间

# 创建PassLib上下文：CryptContext(schemes-加密方案（bcrypt-加密算法）; deprecated-废弃)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme-令牌对象; token: str = Depends(oauth2_scheme)后就是之前加密的令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


# 验证密码: plain_password-普通密码; hashed_password-哈希密码
def verify_password(plain_password: str, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 获取密码哈希
def get_password_hash(password: str):
    # 将JSON对象编码为密集且没有空格的长字符串，相同密码可以转成不同的字符串，但验证都能通过
    return pwd_context.hash(password)

# 获取用户
def get_user(db_name: str, username: str):
    user_dict = db_query(db_name, {"username": username})
    # 判断用户是否存在
    if not user_dict:
        return None
    # 创建用户模型
    return UserInDB(**user_dict) # *表示元组，**表示字典

# 验证用户，成功返回用户信息
def authenticate_user(db_name: str, username: str, password: str):
    user = get_user(db_name, username)
    # 如果用户不存在或者密码错误
    if not user:
        raise_error(404, "用户不存在")
    if not verify_password(decrypt_data(password), user.hashed_password):
        raise_error(401, "密码错误")
    return user # <class '__main__.UserInDB'>

# 创建访问令牌
def create_access_token(username: str, expires_delta:  Optional[timedelta] = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = {
        "sub": username,
    }
    # expire-令牌到期时间
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire}) # {'sub': 用户名, 'exp': datetime.datetime类型时间}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 获取当前用户
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # token加密
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise_error(401, "Could not validate credentials")
            return None
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(USER_DB, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# 获取当前激活用户
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise_error(400, "账户冻结")
        return None
    return current_user

def register_user(db_name: str, username: str, password: str):
    existed_user = get_user(db_name, username)
    if not existed_user:
        db_insert(db_name, {
            "username": username,
            "hashed_password": get_password_hash(decrypt_data(password))
        }, True)
    else:
        raise_error(409, "用户已存在")
    new_user = get_user(db_name, username)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder({"body": new_user})
    )
    # return new_user

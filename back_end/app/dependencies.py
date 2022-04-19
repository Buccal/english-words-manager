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

from model import TokenData, UserInDB, User, CustomException
from decrypt_data import decrypt_data
from db_operation import db_query, db_insert
from config import USER_DB

# 生成随机秘钥命令：openssl rand -hex 32
SECRET_KEY = "9fb2c88349f6ecaf46fd904495a93d132eca5d8c4747ca6ea31910507ed0e8bc"# 密钥
ALGORITHM = "HS256" # 哈希算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 默认访问令牌过期时间

# 创建PassLib上下文：CryptContext(schemes-加密方案（bcrypt-加密算法）; deprecated-废弃)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme-令牌对象; token: str = Depends(oauth2_scheme)后就是之前加密的令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


# 验证密码: plain_password-普通密码; hashed_password-哈希密码
def verify_password(plain_password: str, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 获取密码哈希
def get_password_hash(password: str):
    # 将JSON对象编码为密集且没有空格的长字符串，相同密码可以转成不同的字符串，但验证都能通过
    return pwd_context.hash(password)

# 验证用户，成功返回用户信息
def authenticate_user(db_name: str, username: str, password: str):
    user = get_user(db_name, username)
    # 如果用户不存在或者密码错误
    if not user:
        raise CustomException(code=404, data={ "username": username }, msg="用户不存在")
    if not verify_password(decrypt_data(password), user.hashed_password):
        raise CustomException(code=401, data={ "username": username }, msg="密码错误")
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
    # 返回Bearer令牌：访问令牌的字符串、令牌类型
    raise CustomException(code=200, data={"access_token": encoded_jwt, "token_type": "Bearer", }, msg="获取令牌成功，默认有效时间为%s分钟"%ACCESS_TOKEN_EXPIRE_MINUTES)

# 获取当前用户
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # token解密
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise CustomException(code=401, data={ "token": token }, msg="令牌不完整，信息缺失")
        token_data = TokenData(username=username)
    except JWTError:
        raise CustomException(code=401, data={ "token": token }, msg="令牌有误，解密失败")
    user = get_user(USER_DB, username=token_data.username)
    if user is None:
        raise CustomException(code=401, data={ "username": username }, msg="用户不存在")
    return user

# 获取当前激活用户
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise CustomException(code=400, data=jsonable_encoder(current_user), msg="账户冻结")
    return current_user

# 获取用户
def get_user(db_name: str, username: str):
    user_dict = db_query(db_name, {"username": username})
    # 判断用户是否存在
    if not user_dict:
        return None
    # 创建用户模型
    return UserInDB(**user_dict) # *表示元组，**表示字典

# 用户注册
def register_user(db_name: str, username: str, password:str):
    existed_user = get_user(db_name, username)
    if not existed_user:
        db_insert(db_name, {
            "username": username,
            "hashed_password": get_password_hash(decrypt_data(password)),
            "email": None,
            "words": [],
            "status": "1",
        }, True)
    else:
        raise CustomException(code=409, data={ "username": username }, msg="用户已存在")
    raise CustomException(code=201, data={ "username": username }, msg="用户创建成功")

# 文章分词
def separate_words(context: str):
    formatted_txt = context.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~0123456789“”':
        formatted_txt = formatted_txt.replace(ch, " ")
    return formatted_txt.split()

# 计算词频
def count_words(words: list, exclude: list = []):
    counts = { "known": {}, "new": {} }
    for word in words:
        if len(word) == 1:
            continue
        if word in exclude:
            counts["known"][word] = counts["known"].get(word,0) + 1
        else:
            counts["new"][word] = counts["new"].get(word,0) + 1
#     vue组件有自动排序，取消排序
#     counts["known"] = dict(sorted(counts["known"].items(), key=lambda x: x[1], reverse=True))
#     counts["new"] = dict(sorted(counts["new"].items(), key=lambda x: x[1], reverse=True))
    list = []
    for key in counts["known"]:
        list.append({
            "word": key,
            "count": counts["known"].get(key),
            "isNew": False,
        })
    for key in counts["new"]:
        list.append({
            "word": key,
            "count": counts["new"].get(key),
            "isNew": True,
        })
    return list
    # 返回排序好的二维数组
    # items = list(counts.items())
    # items.sort(key=lambda x:x[1], reverse=True)

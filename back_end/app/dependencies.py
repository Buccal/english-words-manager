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

from model import Token, UserInDB, User, CustomException
from decrypt_data import decrypt_data
from db_operation import db_query, db_insert
from config import USER_DB

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet

# 生成随机秘钥命令：openssl rand -hex 32
SECRET_KEY = "9fb2c88349f6ecaf46fd904495a93d132eca5d8c4747ca6ea31910507ed0e8bc"# 密钥
ALGORITHM = "HS256" # 哈希算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 默认访问令牌过期时间
WNL = WordNetLemmatizer()
WORDNET_MAP = {
    "N": wordnet.NOUN,
    "V": wordnet.VERB,
    "J": wordnet.ADJ,
    "R": wordnet.ADV
}

# 创建PassLib上下文：CryptContext(schemes-加密方案（bcrypt-加密算法）; deprecated-废弃)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme-令牌对象; token: str = Depends(oauth2_scheme)后就是之前加密的令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

# 获取用户
def get_user(db_name: str, username: str):
    user_dict = db_query(db_name, {"username": username})
    # 判断用户是否存在
    if not user_dict:
        return None
    # 创建用户模型
    return UserInDB(**user_dict) # *表示元组，**表示字典

# 获取密码哈希 - 用户注册时用户存储密码
def get_password_hash(password: str):
    # 将JSON对象编码为密集且没有空格的长字符串，相同密码可以转成不同的字符串，但验证都能通过
    return pwd_context.hash(password)

# 用户注册
def register_user(db_name: str, username: str, password:str):
    existed_user = get_user(db_name, username)
    if not existed_user:
        """ print("-----------------------------------------------")
        print(password) # 前端加密的密码
        print(decrypt_data(password)) # 解密的密码：b'123456'
        print(get_password_hash(decrypt_data(password))) # 将密码解析成哈希：$2b$12$hN/D9i6rbJEGG3a52y9kJu/bB4LSQolFcMdnl80O2sYdnQkUWFgxu
        print("-----------------------------------------------") """
        db_insert(db_name, {
            "username": username,
            "hashed_password": get_password_hash(decrypt_data(password)),
            "email": None,
            "words": [],
            "status": "1",
        }, True)
    else:
        return CustomException(code=409, data={ "username": username }, msg="用户已存在")
    return CustomException(code=201, data={ "username": username }, msg="用户创建成功")

# 验证密码: plain_password-普通密码; hashed_password-哈希密码
def verify_password(plain_password: str, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

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
    return CustomException(code=200, data=Token(access_token=encoded_jwt, token_type="Bearer", expire_minutes=ACCESS_TOKEN_EXPIRE_MINUTES), msg="获取令牌成功，默认有效时间为%s分钟"%ACCESS_TOKEN_EXPIRE_MINUTES)

# 用户登录
def login_user(db_name: str, username: str, password: str):
    user = get_user(db_name, username) # <class '__main__.UserInDB'>
    # 如果用户不存在或者密码错误
    if not user:
        return CustomException(code=404, data={ "username": username }, msg="用户名错误")
    if not verify_password(decrypt_data(password), user.hashed_password):
        return CustomException(code=401, data={ "username": username }, msg="密码错误")
    return create_access_token(user.username)

# 获取当前激活用户
async def get_current_active_user(token: str = Depends(oauth2_scheme)):
    # token解密
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise CustomException(code=401, data={ "token": token }, msg="令牌不完整，信息缺失")
    except JWTError:
        raise CustomException(code=401, data={ "token": token }, msg="令牌有误，解密失败")

    current_user = get_user(USER_DB, username=username)
    # 检查用户
    if current_user is None:
        raise CustomException(code=401, data={ "username": username }, msg="用户不存在")
    if current_user.status != 1:
        raise CustomException(code=400, data=jsonable_encoder(current_user), msg="账户异常，请联系管理员")
    return User(**dict(current_user))

# 文章格式化并分词
def separate_words(context: str):
    # 格式化
    formatted_txt = context.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~0123456789“”':
        formatted_txt = formatted_txt.replace(ch, " ")
    # 分词
    tokens = nltk.word_tokenize(formatted_txt)
    # 获取词性
    tokens_with_pos = pos_tag(tokens)
    # 词形还原
    words = []
    for word, tag in tokens_with_pos:
        pos = WORDNET_MAP.get(tag[0])
        if pos is None:
            lemma = WNL.lemmatize(word)
        else:
            lemma = WNL.lemmatize(word, pos)
        words.append(lemma)
    return words

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

def get_user_template_words(db_name: str, level: str, exclude: list[str]):
    template_words = db_query(db_name, {"level": level}, {'_id': 0}, 0, 0)
    if not template_words:
       return CustomException(code=200, data=template_words, msg="ok")
    else:
        for item in template_words.get("data", []):
            item["isKnown"] = True if item["word"] in exclude else False
    return CustomException(code=200, data=template_words, msg="ok")

def get_new_words(old_words: list[str], new_words: list[str])

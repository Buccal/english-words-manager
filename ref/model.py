from pydantic import BaseModel
from typing import Optional

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
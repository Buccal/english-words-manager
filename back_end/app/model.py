from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Union
from bson import ObjectId

# 自定义返回
class CustomException(Exception):
    # __init__用于创建类的实例的方法
    def __init__(self, code: int, data: Union[list, dict, str], msg: Optional[str] = "ok"):
        self.code = code
        self.data = data
        self.msg = msg

# 令牌空壳
class Token(BaseModel):
    access_token: str
    token_type: str
    token_time: int

# 令牌数据
class TokenData(BaseModel):
    username: Optional[str] = None

# 用户基础模型：响应
class User(BaseModel):
    username: str = Field(...)
    email: Optional[EmailStr]
    words: Optional[list] = []
    status: Optional[int] = 1

class UserInfo(BaseModel):
    code: int
    data: User
    msg: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "code": 200,
                "data": {
                    "username": "alice",
                    "email": "alice@example.com",
                    "words": "['apple', 'good', 'box']",
                    "status": "1",
                },
                "msg": "ok"
            }
        }

# 用户更新基础模型：请求
class UpdateUser(BaseModel):
    username: Optional[str] = Field(...)
    hashed_password: Optional[str]
    email: Optional[EmailStr] = ""
    words: Optional[list] = []
    status: Optional[int] = 1

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "alice",
                "hashed_password": "NWewxd6IvYXCTmHKNPzpbkjJdVXQ/pW7H2GaZwSQCTiXYUGK7uhMUCYVCl4tPaxOVR7XEZ2n0MjIe1GyHvRRUoLmcYUFVadYc2+eM5CmPIfzl5P5RnymgJpCPolT1P3jiN0O/ruatofIwQfBOSC+k+mfP5x/i2DmwJH4ZfepXes=",
                "email": "alice@example.com",
                "words": "['apple', 'good', 'box']",
                "status": "1",
            }
        }

# 用户输入数据模型
class UserInDB(User):
    hashed_password: str = Field(...)

class Context(BaseModel):
    userId: Optional[str]
    content: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "content": "alice",
                "hashed_password": "NWewxd6IvYXCTmHKNPzpbkjJdVXQ/pW7H2GaZwSQCTiXYUGK7uhMUCYVCl4tPaxOVR7XEZ2n0MjIe1GyHvRRUoLmcYUFVadYc2+eM5CmPIfzl5P5RnymgJpCPolT1P3jiN0O/ruatofIwQfBOSC+k+mfP5x/i2DmwJH4ZfepXes=",
                "email": "alice@example.com",
                "words": "['apple', 'good', 'box']",
                "status": "1",
            }
        }

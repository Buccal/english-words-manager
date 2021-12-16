from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId

# _id主键
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# 令牌空壳
class Token(BaseModel):
    access_token: str
    token_type: str

# 令牌数据
class TokenData(BaseModel):
    username: Optional[str] = None

# 用户基础模型：响应
class User(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    email: Optional[EmailStr]
    disabled: Optional[bool] = False

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "alice",
                "email": "alice@example.com",
                "disabled": "False",
            }
        }

# 用户更新基础模型：请求
class UpdateUser(BaseModel):
    username: Optional[str] = Field(...)
    hashed_password: Optional[str]
    email: Optional[EmailStr]
    disabled: Optional[bool] = False

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "alice",
                "hashed_password": "NWewxd6IvYXCTmHKNPzpbkjJdVXQ/pW7H2GaZwSQCTiXYUGK7uhMUCYVCl4tPaxOVR7XEZ2n0MjIe1GyHvRRUoLmcYUFVadYc2+eM5CmPIfzl5P5RnymgJpCPolT1P3jiN0O/ruatofIwQfBOSC+k+mfP5x/i2DmwJH4ZfepXes=",
                "email": "alice@example.com",
                "disabled": "False",
            }
        }

# 用户输入数据模型
class UserInDB(User):
    hashed_password: str = Field(...)
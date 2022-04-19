import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio

app = FastAPI()

# 1. 连接数据库
MONGODB_URL="mongodb://localhost"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.college


# FastAPI使用JSON处理数据，无法直接解析ObjectId，所以先转成string
# MongoDB存储数据的格式为BSON，它支持非JSON数据类型，如ObjectId
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

# MongoDB有着非常灵活的模式，默认不执行文档结构，可以根据程序和性能选择模型。如下面两个模型：StudentModel和UpdateStudentModel

# StudentModel模型常被用于响应请求
# MongoDB使用_id作为主键，但Python语法会将_开头属性作为私有变量，无法进行赋值，所以模型中添加了别名id
class StudentModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    gpa: float = Field(..., le=4.0)

    # https://pydantic-docs.helpmanual.io/usage/model_config/
    class Config:
        # 是否包含别名
        allow_population_by_field_name = True
        # 是否允许任意类型
        arbitrary_types_allowed = True
        # 自定义类型编码为JSON的方式
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }

# UpdateStudentModel模型常没有id属性，且所有字段可选
class UpdateStudentModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    course: Optional[str]
    gpa: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }

# 创建一个新学生
@app.post("/", response_description="Add new student", response_model=StudentModel)
async def create_student(student: StudentModel = Body(...)):
    # 1. 以JSON形式接收参数
    # 2. 在操作数据库之前将参数解码为Python字典
    student = jsonable_encoder(student)
    # 插入新学生信息，返回新学生id
    new_student = await db["students"].insert_one(student)
    # 使用新学生id查找新学生信息
    created_student = await db["students"].find_one({"_id": new_student.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)

# 获取所有学生的信息列表
@app.get(
    "/",
    response_description="List all students",
    response_model=List[StudentModel]
)
async def list_students():
    # to_list(文档总数)
    # 实际开发中：find(skip, limit)
    students = await db["students"].find().to_list(1000)
    return students

# 获取单个学生的信息
@app.get(
    "/{id}",
    response_description="Get a single student",
    response_model=StudentModel
)
async def show_student(id: str):
    # 条件赋值表达式（海象运算符）
    if (student := await db["students"].find_one({"_id": id})) is not None:
        return student
    raise HTTPException(status_code=404, detail=f"Student {id} not found")

# 更新学生的信息
@app.put("/{id}", response_description="Update a student", response_model=StudentModel)
async def update_student(id: str, student: UpdateStudentModel = Body(...)):
    # 筛除值为空的键
    student = {k: v for k, v in student.dict().items() if v is not None}
    # 如果有值，更新并返回最新的信息
    if len(student) >= 1:
        update_result = await db["students"].update_one({"_id": id}, {"$set": student})

        if update_result.modified_count == 1:
            if (
                updated_student := await db["students"].find_one({"_id": id})
            ) is not None:
                return updated_student
    # 如果没有值，返回学生当前信息
    if (existing_student := await db["students"].find_one({"_id": id})) is not None:
        return existing_student
    # 如果查找不到这个学生，报错404
    raise HTTPException(status_code=404, detail=f"Student {id} not found")

# 删除学生
@app.delete("/{id}", response_description="Delete a student")
async def delete_student(id: str):
    delete_result = await db["students"].delete_one({"_id": id})
    # 成功删除，返回204状态
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    # 如果查找不到这个学生，报错404
    raise HTTPException(status_code=404, detail=f"Student {id} not found")

    # [Introducing FARM Stack - FastAPI, React, and MongoDB](https://www.mongodb.com/developer/how-to/FARM-Stack-FastAPI-React-MongoDB/)

# -------------------------------------

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# tokenUrl：客户端用来发送用户名和密码来获取token的url
# "token"是个相对url（相对要注意有代理的情况），等价于"./token"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Authorization: Bearer 3ebd3e8b-a8af-4674-84e3-7eba87e8e34a

# OAuth2PasswordBearer实例是一个回调
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
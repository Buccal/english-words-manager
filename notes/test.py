import pymongo
client = pymongo.MongoClient("localhost")
db = client["Words_Manager"]
user = db["user"]

""" def to_list_or_dict(cursor):
    new_list = list(cursor)
    count = len(new_list)
    if(count == 0):
        return None
    if(count == 1):
        return new_list[0]
    else:
        return {
            "count": count,
            "data": new_list
        }

result = user.find({"username": "test"})
query_result = to_list_or_dict(result)
print(query_result) """

from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    username: str
    words: list[str] = []
    status: int = 1

class UserInDB(User):
    hashed_password: str = ""

user = {
    "username": "lily",
    "password": "123"
}

print(UserInDB(**user, hashed_password = user["password"]))

# def test(arg: UserInDB):
#     print(arg)
#
# test(user)

class Foo(BaseModel):
    name1: str = None
    name2: Optional[str]
    name3: Optional[str] = None
    defaulted_list_field: list[str] = ["a"]

f1 = Foo(defaulted_list_field=["b"])

print(f1)

class STRUCTURE_NAME(BaseModel):
    name1: str = None
    name2: Optional[str]
    name3: Optional[str] = None
print(STRUCTURE_NAME())


class Animal(BaseModel):
    hasTail: bool = False

class Cat(Animal):
	name: str = "mimi"

print(Cat(hasTail = True, name = "Kitty")) # hasTail=True name='Kitty'
print(Cat(**{ "hasTail": True, "name": "Kitty"})) # hasTail=True name='Kitty'
print(Cat(**{ "hasTail": True}, name = "Kitty")) # hasTail=True name='Kitty'























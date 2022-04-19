import pymongo
client = pymongo.MongoClient("localhost")
db = client["Words_Manager"]
user = db["user"]

def to_list_or_dict(cursor):
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

result = user.find({"user_name": "test"})
query_result = to_list_or_dict(result)
print(query_result)

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    words: list = []
    status: Optional[int] = 1

class UserInDB(User):
    hashed_password: str = ""

user = {
    "username": "lily",
    "password": "123"
}

def test(arg: UserInDB):
    print(arg)

test(user)

# 安全的哈希密码库
# JWT令牌
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
  "johndoe": {
    "username": "johndoe",
    "full_name": "John Doe",
    "email": "johndoe@example.com",
    "hashed_password": "fakehashedsecret",
    "disabled": False,
  },
  "alice": {
    "username": "alice",
    "full_name": "Alice Wonderson",
    "email": "alice@example.com",
    "hashed_password": "fakehashedsecret2",
    "disabled": True,
  },
}

app = FastAPI()

def fake_hash_password(password: str):
  return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
  username: str
  email: Optional[str] = None
  full_name: Optional[str] = None
  disabled: Optional[bool] = None

class UserInDB(User):
  hashed_password: str

# *表示元组，**表示字典
def get_user(db, username: str):
  if username in db:
    user_dict = db[username]
    return UserInDB(**user_dict)

def fake_decode_token(token):
  # This doesn't provide any security at all
  # Check the next version
  # token = alice
  user = get_user(fake_users_db, token)
  return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
  user = fake_decode_token(token)
  # 判断用户是否存在
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid authentication credentials",
      # 规范要求
      headers={"WWW-Authenticate": "Bearer"},
    )
  return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
  # current_user = username='alice' email='alice@example.com' full_name='Alice Wonderson' disabled=True hashed_password='fakehashedsecret2'
  # 为啥可以直接.取？
  # 判断用户是否启用
  if current_user.disabled:
    raise HTTPException(status_code=400, detail="Inactive user")
  return current_user

# 获取令牌
@app.post("/token")
# OAuth2PasswordRequestForm是一个类依赖项项，声明了如下的请求表单：
# - username
# - password
# - grant_type：可选
# - scope：可选，是一个由空格分隔的字符串组成的大字符串
# - client_id：可选
# - client_secret：可选
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
  # 用户是否存在：Dict.get(key)
  user_dict = fake_users_db.get(form_data.username)
  if not user_dict:
    raise HTTPException(status_code=400, detail="用户名错误")

  # 密码是否正确
  user = UserInDB(**user_dict) #为什么要有这一步？类型检查？
  # 上传密码加密
  hashed_password = fake_hash_password(form_data.password)
  if not hashed_password == user.hashed_password:
    raise HTTPException(status_code=400, detail="密码错误")

  # 返回Bearer令牌：访问令牌的字符串、令牌类型
  return {"access_token": user.username, "token_type": "bearer"}

# 查询用户本人的信息
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
  return current_user

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("security:app", host="127.0.0.1", port=8000, reload=True)

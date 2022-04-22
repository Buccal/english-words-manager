## 启动
1. 进入`init`目录，运行以下命令初始化数据库
   - `python setup_user.py`
   - `python setup_word.py`
2. 进入`app`目录，运行`python main.py`启动接口

## 目录结构

### APP
```Tree
|____ app
     |____config.py - MONGODB和RSA密钥的设置文件
     |____db_operation.py - 操作数据库的方法
     |____decrypt_data.py - RSA密钥解密
     |____dependencies.py - 业务相关的方法
     |____main.py - 定义接口、启动入口
     |____model.py - 数据模型
     |____my_private_rsa_key.pem - 私钥
     |____my_public_rsa_key.pem -公钥 
     |____response_info.py - 返回信息
```

### init
```Tree
|____ init
     |____create_rsa_key.py - 提供了生成RSA密钥、加密、解密的功能
     |____setup_user.py.py - 初始化用户表，添加管理员账号
     |____setup_word.py - 初始化单词列表，添加了小学、中学、高中标准词汇
```

## 参考
[Swagger UI](http://127.0.0.1:8000/docs)

## 学习笔记

### 如何使用BaseModel

1. 基本语法
```python
from pydantic import BaseModel

class STRUCTURE_NAME(BaseModel):
    FIELD: TYPE = DEFAULT_VALUE
```

2. 常见数据类型
```python
from pydantic import BaseModel, Field, EmailStr

class Parent(BaseModel):
    mom: str
    dad: str

class Kid(BaseModel):
    name: str
    age: int
    number: long
    hobby: list[str]
    email: EmailStr
    parent: Parent
```

3. 可选值、默认值
```python
class STRUCTURE_NAME(BaseModel):
    name1: str = None
    name2: Optional[str]
    name3: Optional[str] = None
print(STRUCTURE_NAME())
```
输出：`name1=None name2=None name3=None`

4. 传参
```python
class Animal(BaseModel):
    hasTail: bool = False

class Cat(Animal):
	name: str = "mimi"

print(Cat(hasTail = True, name = "Kitty")) # hasTail=True name='Kitty'
print(Cat(**{ "hasTail": True, "name": "Kitty"})) # hasTail=True name='Kitty'
print(Cat(**{ "hasTail": True}, name = "Kitty")) # hasTail=True name='Kitty'
```


5. 对字段进行校验
```python
from pydantic import BaseModel, Field
class Hoo(BaseModel):
    name: str = Field("book", description="name must be less than 10", title="book name", max_length=10)
    price: int = Field(20, gt=0, description="price must be greater than 0", title="good price")

print(Hoo(price = -50)) #error
print(Hoo(name = "popular books")) #error
```
### 接口返回方式
1. 直接return，不管返回code时多少，都会被axios以onFulfilled捕获
```python
return {
   "code": 404,
   "data": None,
   "msg": "dddddd"
}
```

```js
axios.interceptors.response.use(res=>{}, err=>{
  // 在这里被捕获
})
```

2. raise Exception
    - code以2开头：被axios以onFulfilled捕获
    - code以其他数字开头：被axios以onRejected捕获
```python
raise CustomException(code=201, data=None, msg="dddddd")
```

```js
axios.interceptors.response.use(res=>{
  // 在这里被捕获
}, err=>{})
```

## 处理逻辑

### 路由守卫拦截
    若有Token
        若请求的是登录地址：继续导航
        若请求的是其他地址 Todo
            若有权限信息
                若访问地址在权限内：继续导航
                若访问地址不在权限内：提示错误
            若无权限信息：请求权限信息
                若请求权限信息成功：回到上一步
                若请求权限信息失败：执行登出，重定向到登录页
    若无Token
        若请求地址在免登录白名单里：继续导航
        若请求地址不在免登录白名单里：重定向到登录页

### 请求响应拦截
请求拦截
    若为登录注册接口，加密密码，单独处理请求
    若为其他接口
        若有Token：添加Authorization
        若为get请求：处理传参
响应拦截
    正常返回
        映射错误信息
        若返回401：提示登录过期，跳转到登录页
        若返回非2开头：设置接口返回结果为失败
        其他：设置接口返回结果为成功
    疫情返回
        处理异常错误

### 注册逻辑
1. 根据用户名查询数据库判断用户是否存在
2. 若用户不存在
   1. 使用decrypt_data解密密码
   2. 再使用get_password_hash转为哈希
   3. 然后插入新用户数据
3. 若用户已存在：返回409

### 登录逻辑
1. 根据用户名查询数据库判断用户是否存在
2. 若用户不存在：返回404
   1. 获取用户的哈希密码
   2. 使用decrypt_data解密密码
   3. 使用verify_password验证两者是否一致
   4. 若验证失败：返回401
   5. 若验证成功，使用create_access_token根据用户名、过期时间生成token并返回

### 其他接口验证token逻辑
1. token解密
2. 若解密失败：返回401
3. 若用户名为空：返回401
4. 根据用户名查询数据库判断用户是否存在
5. 若用户不存在：返回401
6. 若用户状态异常：返回400

## Todo
-[] 数据库操作没有加try catch
-[] （哈希）密码和 JWT Bearer 令牌具体逻辑


























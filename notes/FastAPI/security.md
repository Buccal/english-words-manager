# 安全

## 获取令牌

1. 传入form_data
    ```json
    {
      "username": "alice",
      "password": "aaasss"
    }
    ```
2. 判断用户是否存在：使用username去数据库查询
3. 获取并验证数据库中此用户的信息，创建用户模型UserInDB（子依赖User）
    ```python
    {
      "username": "alice",
      "email": "alice@example.com",
      "hashed_password": "$2b$12$MP0NyRYuGkOFTrVBBtuH4O63cAEz8OPtsNCcjwB9eFn0YCzyMjJ6K",
      "disabled": False,
    }
    ```
5. 验证密码是否正确：password、hashed_password
6. 计算令牌到期的时间点
7. 添加令牌内容：用户名和时间点
    ```python
    {
      "sub": "alice",
      "exp": datetime.datetime(20021, 12, 14, 15, 30, 00, 00000)
    }
    ```
8. 编码令牌内容，获得令牌
`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGljZSIsImV4cCI6MTYzOTQ2NjkyMX0.qNn_YupQCrRwKder9bViPRaJk6dE7RBucPYPvAsqd8Y`
9. 验证令牌，创建令牌模型Token
    ```python
    {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGljZSIsImV4cCI6MTYzOTQ2NjkyMX0.qNn_YupQCrRwKder9bViPRaJk6dE7RBucPYPvAsqd8Y",
      "token_type": "bearer"
    }
10. 返回令牌模型


## 请求授权信息

1. 在请求头中添加字段
`Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGljZSIsImV4cCI6MTYzOTQ2NjkyMX0.qNn_YupQCrRwKder9bViPRaJk6dE7RBucPYPvAsqd8Y`
2. 自动获取token
`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGljZSIsImV4cCI6MTYzOTQ2NjkyMX0.qNn_YupQCrRwKder9bViPRaJk6dE7RBucPYPvAsqd8Y`
3. 解码token，获得用户名
4. 判断用户名是否为空
5. 验证用户名，创建令牌数据模型TokenData
6. 判断用户是否存在：使用用户名去数据库查询
7. 获取并验证数据库中此用户的信息，创建用户模型UserInDB（子依赖User）
8. 判断用户是否被禁用

> 没有验证令牌过期时间？但刚刚令牌确实失效了，是自动判断的？




























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

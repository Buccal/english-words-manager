#!/usr/bin/env python3
# coding=utf-8

# 从 Crypto.PublicKey 包中导入 RSA
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP, PKCS1_v1_5

from config import PASSPHRASE, PRIVATE_RSA_KEY, PUBLIC_RSA_KEY

# 创建RSA密钥
def create_rsa_key(passphrase=PASSPHRASE):
    # 生成 1024/2048 位的 RSA 密钥
    key = RSA.generate(1024)
    # 调用 RSA 密钥实例的 exportKey 方法创建私钥
    encrypted_key = key.exportKey(
        passphrase=passphrase, # 密码
        pkcs=8, # 使用的 PKCS 标准
        protection="scryptAndAES128-CBC" # 加密方案
    )
    # 将私钥写入磁盘的文件
    with open(PRIVATE_RSA_KEY, "wb") as f:
        f.write(encrypted_key)
    # 使用方法链调用 publickey 和 exportKey 方法生成公钥，写入磁盘上的文件
    with open(PUBLIC_RSA_KEY, "wb") as f:
        f.write(key.publickey().exportKey())

# 使用公钥加密
def encrypt(context: bytes, passphrase=PASSPHRASE):
    # 加载公钥
    recipient_key = RSA.import_key(
        open(PUBLIC_RSA_KEY).read()
    )
    cipher_rsa = PKCS1_v1_5.new(recipient_key)

    # 加密
    en_data = cipher_rsa.encrypt(context)

    return en_data

def decrypt(context, passphrase=PASSPHRASE):
    # 读取密钥
    private_key = RSA.import_key(
        open(PRIVATE_RSA_KEY).read(),
        passphrase=passphrase
    )
    cipher_rsa = PKCS1_v1_5.new(private_key)

    # 解密
    de_data = cipher_rsa.decrypt(context, None)

    return de_data


if __name__ == '__main__':
    # 创建非对称秘钥对
    # 也有密钥对在线生成网站：http://web.chacuo.net/netrsakeypair
    create_rsa_key()

    """
    # 测试加密功能
    test_info = "12asfsd.wqi"
    en_test_info = encrypt(test_info.encode('utf-8'))
    print(en_test_info)

    # 测试解密功能
    de_test_info = str(decrypt(en_test_info), encoding = "utf-8")
    print(de_test_info)

    # 验证加密解密后内容是否一致
    print(test_info == de_test_info)
    """
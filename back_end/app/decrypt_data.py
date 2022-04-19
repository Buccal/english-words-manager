# 导入RSA加密包
from Cryptodome.PublicKey import RSA
# 导入签名方案
from Cryptodome.Cipher import PKCS1_v1_5
import base64

# 导入配置
from config import PASSPHRASE, PRIVATE_RSA_KEY

# 解密函数
def decrypt_data(inputdata, passphrase=PASSPHRASE):
    data = base64.b64decode(inputdata)

    private_key = RSA.import_key(
        open(PRIVATE_RSA_KEY).read(),
        passphrase=passphrase
    )

    cipher_rsa = PKCS1_v1_5.new(private_key)

    sentinel = None
    # 当解密失败，会返回 sentinel
    ret = cipher_rsa.decrypt(data, sentinel)

    return ret
    # return str(ret, encoding = "utf-8")

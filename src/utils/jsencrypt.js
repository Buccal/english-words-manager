import JSEncrypt from 'jsencrypt/bin/jsencrypt.min'

// 公钥
const publicKey = `
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4ignIO8MHaov0tajx4CDY2lJV
iZIcmDbNy0DMbI0TuB4YOKQhyqLQhzojBUCxGOvnulKyGEbkDA/U/IYvVu5GBR7m
aAq5B9InXjciaOyhCmQ+5FLCUPMGRPnDmZRa2E+13XTerofniq3GjdrNA/lyuNL0
vAOb/ANp2n2MsrNvSwIDAQAB`

// 私钥
const privateKey = `
MIIC1TBPBgkqhkiG9w0BBQ0wQjAhBgkrBgEEAdpHBAswFAQIwHbIb+bTd3ACAkAA
AgEIAgEBMB0GCWCGSAFlAwQBAgQQONpFq1bvQAJjnFix3U5xqASCAoBb62bLtlqR
Zgv7/OrzjcYYnUVoPmrrl+KzHwGdLY4J2E5TqkHI5MMhOYsoskCCcnDVYponuWj5
0JYfcxI9+FZ4WTAtRenH6hHIuS3yggBVcy5qLfuEMte7OhZ8Zcdj4QmMnsc+hyEq
r+HygoiTdjk6qOquo/dhsgnl0mLVh26vL1mCL5hkcohd6Z8TaLImoaJKLaIc6Cyx
ssL5VCFx0mPHEV3BEq44ddEXoerchcQlK5KK0OUPCUd6Y9Gdw1uisa9lE4rGv6vD
qLf7rHBTccQax88umaytOmy+XNYG1uC4d8pQbcWm72wpuERJIuUrwKGaDdSwSbKk
bqMZyRrgBhsehBHB4t6t93ViI0FkxgdpzdLsIKwUmLCL8m/JEYsjmzmhZBHJbYxK
PCe6D8No63rt4+zD4Ljui6XuqFlbF6/PGpyCS5badG1IrPJ43ezkjy9N34A7guXT
c4W2sRfEVzm1WsJaX6UPRbrHiAfFB8Aj4eDA2QgZ3msy4YQfnskc1pHlqFXX/dA5
k1lRJLyH4cVkAkn7dsk+JxTfzED/mTk3oWxwtbAVaqe8V+xIWyQftND18yKQc93D
bVdygVDNwvhMp4F7dmaBR/ksFjIymSzQ9k0qaP/rx5JLzQUVA0U5mILrZY3otbV3
9PaWiy5kdI5iAuRuVmzvqdtqqS6Wk9nbx5NROOgU7oqQ1XSrqkgjfXaabaKquXFG
aazw9YQXOWQJmke+9R8W0s5CHLl3hAN8i49Zquxw2SZnpN2+zqddC7jWRKK9Mvth
B5a5vDdh5oqJGiBCDFwEQ0KfEYfFJIXicE3YmVwf2paqKlTmXI15wjhKPvgw5Che
XYdCs0f6Lamh`

// 加密
export function encrypt (content) {
  const encryptor = new JSEncrypt()
  encryptor.setPublicKey(publicKey) // 设置公钥
  return encryptor.encrypt(content) // 对数据进行加密
}

// 解密
export function decrypt (content) {
  const encryptor = new JSEncrypt()
  encryptor.setPrivateKey(privateKey) // 设置私钥
  return encryptor.decrypt(content) // 对数据进行解密
}

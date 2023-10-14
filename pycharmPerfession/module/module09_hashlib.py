#加密算法  md5  sha1  sha256  单项加密
#

import hashlib

msg = '你好 数理统计方法'

md5 = hashlib.md5(msg.encode('utf-8'))
sha1 = hashlib.sha1(msg.encode('utf-8'))
sha224 =hashlib.sha224(msg.encode('utf-8'))
sha256 =hashlib.sha256(msg.encode('utf-8'))
sha512 = hashlib.sha512(msg.encode('utf-8'))
print(md5.hexdigest())
print(sha1.hexdigest())
print(sha224.hexdigest())
print(sha256.hexdigest())
print(sha512.hexdigest())
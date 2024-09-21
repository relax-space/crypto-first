from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# 生成一个随机的16字节密钥
key = get_random_bytes(16)

# 要加密的数据
data = b"Hello, AES encryption!"

# 创建一个 AES 对象
cipher = AES.new(key, AES.MODE_CBC)

# 加密数据
ciphertext = cipher.encrypt(pad(data, AES.block_size))

# 将加密后的数据转换为 Base64 编码的字符串
b64_ciphertext = base64.b64encode(ciphertext)

# 打印 Base64 编码的加密数据
print("Base64 Ciphertext:", b64_ciphertext)

# 将 Base64 编码的加密数据转换为二进制数据
b64_ciphertext_bytes = base64.b64decode(b64_ciphertext)

print("b64_ciphertext_bytes", b64_ciphertext_bytes)

# 解密数据
decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
print(base64.b64encode(cipher.iv).decode("utf8"))
plaintext = unpad(decipher.decrypt(b64_ciphertext_bytes), AES.block_size)

# 打印解密后的数据
print("Plaintext:", plaintext)

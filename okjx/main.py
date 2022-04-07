'''
    说明: 加密和解密的例子, 都能看懂,不多做解释
'''
from base64 import b64decode, b64encode

import execjs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class CryptoR():

    def __init__(self, key: str, iv: str):
        self.aes = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))

    def encrypto(self, text: str) -> str:
        p = pad(text.encode('utf8'), AES.block_size)
        return b64encode(self.aes.encrypt(p)).decode('utf8')

    def decrypto(self, text: str) -> str:
        d = self.aes.decrypt(b64decode(text))
        return unpad(d, AES.block_size).decode('utf8')


def crypto_js(func_name: str, text: str, key: str, iv: str) -> str:
    with open('okjx/js/crypto_m.js', mode='r', encoding='utf8') as f:
        ctx = execjs.compile(f.read())
    return ctx.call(func_name, text, key, iv)


def call_en():
    text = 'm3u8.okjx.cc|057f1eed099f2f7e'
    key = 'dvyYRQlnPRCMdQSe'
    iv = '057f1eed099f2f7e'
    aes = CryptoR(key, iv)
    e1 = aes.encrypto(text)
    e2 = crypto_js('encrypt', text, key, iv)
    assert e1 == e2 == 'ncZvyrJ2IPdKSF2EmvfZAGVrtAj9D8eXnGpjPTV1QTM=', 'encrypto error'


def call_de():
    text = 'hFsaNOHoCwp4I3+MicxRQTLiyeIwIALznU6YEuLcAmFyts3Yt9IfHc/JY94i4NVzyXMCfL2gaW88KskGpnUPl35HcLzMZJfohnaiu5/m/6ObssUfugjS/0UlGgcOJsb5ZFptWNFXuLJQzvyZc5WD9t/Zf/yRynRBdSHG4GMN2+fcGCsiP5uhm2ZYrx0UTjL1KwpryPim8jPMNztj+h6ehwQmqAiRCohtOsssw40csh++yqQJqXECiiJ/9mmcI0Fe'
    key = '36606EE9A59DDCE2'
    iv = '057f1eed099f2f7e'
    aes = CryptoR(key, iv)
    d1 = aes.decrypto(text)
    d2 = crypto_js('decrypt', text, key, iv)
    d2 = unpad(d2.encode('utf8'), AES.block_size).decode('utf8')
    d3 = 'https://json.nbjx.vip:4399/hls/4b7ce0c8460c437037918dcb5f3a8818.m3u8?vkey=c097V4ps90g9CpK5DX70N07deE2YIE-4i8wTq574P1YnQ68pv-rQGNV2wW0mHWsvBwClWONt_K5jIimrTiuQ3xrifwDMSYGDjUdskwLH2X9J2n-OnA'
    assert d1 == d2 == d3, 'decrypto error'


def main():
    call_en()
    call_de()


if __name__ == '__main__':
    main()

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
    text = 'HCizZLcgJfm1LvajcEBMHChheUySaJgXpuPL+L9BDW4jdd9ds5qCycVwN6SpotDujY/tok+sT2M//AeeKnDk6TrZ0gvFa1szUi8j3xg2TTZXZMW/52wuXhr1vnxrbrz4socZ2twSY1T63NiJx3XAcLe6RXfSmBxuPzstMQ0pDSSDNPT4H5hKYy1wo227zzcnxdAuwo1WTvcdaMIuXBS/9IkbqNFklzikvvdGjJjsVxRLwSd5T6v4I47CUAgVtncxpf3cKlM37lmEWpZwskJKG/IGkJRRy9K2a/tdIMWNu0JbsF0jlyMNT/kT2OS08jsRsGJPxOnpEiFIPgE6UPGUgq7+SaBHvFdSfusdqDTwBHuyXJTZBixolYEnggfr3UfWOtP1pvWR4R7bY2N7XJ7gEf6QMfjbu0YB1V4+2WX5ucy43954EniGFbUw2Zxi35y+OGgkpunPTzccVbGw871RjiU7iNVo+IXvQHgG+0FPjaWUezWYm4YAePohtxJYAqg+1XATcgFOKTUn21QQCDKAuQ=='
    key = '0EAE7A71512EC09C'
    iv = '675480787382e6f4'
    aes = CryptoR(key, iv)
    d1 = aes.decrypto(text)
    d2 = crypto_js('decrypt', text, key, iv)
    d2 = unpad(d2.encode('utf8'), AES.block_size).decode('utf8')
    d3 = 'https://subtitle.apdcdn.tc.qq.com/vipzj.video.tc.qq.com/gzc_1000102_0b53o4aagaaa2eaerjcv5zrma56dan5qab2a.f2.mp4?vkey=5DD8A1F1C4657D16EE8F61CEA9D4FEDF5195B3F0404A4104E6877F4D61D6DF3F02B8EA021782BFF03319989D91AF586088584D8DB58C6908C6B83C02137CE54CB3F09873AC784EFB2D24A2A4D041757D7E753A5523BB08AC010E33F4DD1F8A16F8266900BA457AF5223DB94A6187A6280CEA7CCA4BF76EDC&QQ=335583&From=www.nxflv.com'
    assert d1 == d2 == d3, 'decrypto error'


def main():
    call_en()
    call_de()


if __name__ == '__main__':
    main()

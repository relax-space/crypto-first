'''
说明: 例子仅仅说明pkcs7的原理, 略去了合法性检测的部分
测试整个文件: pytest -vs pad_sample/pad_.py
测试单个方法
pytest -vs pad_sample/pad_.py::test_pad
pytest -vs pad_sample/pad_.py::test_unpad


    基础: 
        1. 1个字节有8位, 所以128位是16个字节
        2. 一个字母就是一个字节,一个汉字是两个字节
        3. 16进制: 0-9, a,b,c,d,e,f, 其中a代表10,后面依次加1, 满16进一,所以 15对应\x0d,16对应\x10
    pkcs7补位规则: 
        1. 不足16位字节的倍数,补足变成16位的倍数
        2. 如果刚好是16的倍数, 补16个字节
        3. 补位的数:
            1. unicode: 假如需要补1个字节,1对应unicode编码, 则 chr(1)) 结果是 \x01
            3. int:  unicode转换为整型的方法, ord('\x11')值为17
        4. 补充的值: 
            1. 等于补位的数量, 比如:content有9位,那么补充7个字节,每个字节的值都是\x06
            2. 补充的值,整数的unicode编码,类似16进制
            
'''


def pad(content: str, block_size: int = 16) -> str:
    p_len = block_size - len(content) % block_size
    p = p_len * chr(p_len)
    return content + p


def unpad(content: str) -> str:
    last_char = ord(content[-1])
    # 逆着取数, 但是打印的时候,还是顺着打印的
    return content[:-last_char]


def test_pad():
    # 计算字节数
    assert 3 == len('11中'), 'pad china error'
    assert 4 == len('abcd'), 'pad china error'

    p1 = pad('1')
    assert '1\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f' == p1, 'pad 1 error'

    b = r'1\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'
    assert f"'{b}'" == repr(p1), 'pad 1 1 error'

    p2 = pad('11')
    assert '11\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e' == p2, 'pad 2 error'

    p15 = pad('111111111122222')
    assert '111111111122222\x01' == p15, 'pad 15 error'

    p16 = pad('1111111111222222')
    assert '1111111111222222\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10' == p16, 'pad 16 error'


def test_unpad():
    p1 = '1\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f'
    assert '1' == unpad(p1)

    p2 = '11\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
    assert '11' == unpad(p2)

    p15 = '111111111122222\x01'
    assert '111111111122222' == unpad(p15)

    p16 = '1111111111222222\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'
    assert '1111111111222222' == unpad(p16)

"""
说明: 为什么要PKCS7填充? 因为PKCS7是当下各大加密算法都遵循的数据填充算法
测试整个文件: pytest -vs pad_sample/pad_.py
测试单个方法
pytest -vs pad_sample/pad_.py::test_pad
pytest -vs pad_sample/pad_.py::test_unpad


    基础: 
        1. 1个字节有8位, 所以16个字节是128位, 比如: 一个字母A就是一个字节
        2. 16进制: 0-9, a,b,c,d,e,f, 其中a代表10,后面依次加1, 满16进一,所以 10进制15对应的16进制是0x0f,16对应0x10
        3. 转换: 
            int -> unicode, chr(1) 结果是 \x01
            unicode -> int, ord('\x11')值为17
    pkcs7补位规则: 
        1. 补位的个数: 不足16位字节的倍数,补足变成16位的倍数,如果刚好是16的倍数, 补16个字节
        2. 补位的值: 等于补位个数的unicode码, 比如:content有7位,那么补充9个字节,每个字节的值都是\x09
        
    补位的好处:
        方便获取真实字符串: 直接获取字符串的最后一个字符,转换为int即为补位的数, 然后,真实 = 原始字符串长度 - 补位的数  
            
"""


def pad(content: str, block_size: int = 16) -> str:
    p_len = block_size - len(content) % block_size
    p = p_len * chr(p_len)
    return content + p


def unpad(content: str) -> str:
    last_char = ord(content[-1])
    # 获取真实字符串,去掉最后补位的数据
    return content[:-last_char]


def test_pad():
    # 计算字节数
    assert 3 == len("11中"), "pad china error"
    assert 4 == len("abcd"), "pad china error"

    p1 = pad("1")
    assert (
        "1\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f" == p1
    ), "pad 1 error"

    b = r"1\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f"
    assert f"'{b}'" == repr(p1), "pad 1 1 error"

    p2 = pad("11")
    assert (
        "11\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e" == p2
    ), "pad 2 error"

    p15 = pad("111111111122222")
    assert "111111111122222\x01" == p15, "pad 15 error"

    p16 = pad("1111111111222222")
    assert (
        "1111111111222222\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10"
        == p16
    ), "pad 16 error"


def test_unpad():
    p1 = "1\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f"
    assert "1" == unpad(p1)

    p2 = "11\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e"
    assert "11" == unpad(p2)

    p15 = "111111111122222\x01"
    assert "111111111122222" == unpad(p15)

    p16 = "1111111111222222\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10"
    assert "1111111111222222" == unpad(p16)

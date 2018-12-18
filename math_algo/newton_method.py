# coding=utf-8


# 牛顿迭代法求平方根
from math import sqrt


def newton_sqrt(num):
    if num < 0:
        return None
    count = 1
    num = num * 1.0
    ret = num / 2.0
    while abs(ret ** 2 - num) > 0.000001:  # 注意这里要取绝对值
        print count, ret
        count += 1
        ret = (ret + num / ret) / 2  # 迭代公式
    return ret


if __name__ == '__main__':
    print sqrt(5)
    print newton_sqrt(5)

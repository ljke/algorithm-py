# coding=utf-8

# 动态规划解决爬楼梯问题，也就是斐波那契数列
from time import time


# 递归法
def get_climbing_way_1(n):
    # type: (int) -> int
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return get_climbing_way_1(n - 1) + get_climbing_way_1(n - 2)


# 备忘录法
def get_climbing_way_2(n, record):
    # type: (int, dict) -> int
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        item = record.get(n)
        if item:
            return item
        else:
            value = get_climbing_way_2(n - 1, record) + get_climbing_way_2(n - 2, record)
            record[n] = value
            return value


# 动态规划, 斐波那契数列求解，递推方式和爬楼梯问题相反
def get_climbing_way_3(n):
    # type: (int) -> int
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        temp = 0

        for i in range(3, n + 1):
            temp = a + b
            a = b
            b = temp

        return temp


if __name__ == '__main__':
    n = 20
    start = time()
    print get_climbing_way_1(n)
    end = time()
    print end - start

    start = time()
    record = {}
    print get_climbing_way_2(n, record)
    end = time()
    print end - start

    start = time()
    print get_climbing_way_3(n)
    end = time()
    print end - start

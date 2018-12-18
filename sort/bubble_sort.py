# coding=utf-8

# 冒泡排序


def bubble_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    # i, j取值可以有多种写法
    # for i in range(len(arr))
    # for j in range(len(arr) - i - 1)
    for i in range(length-1, 1, -1):  # 倒序的写法range(max, min, -1)
        flag = False  # 注意位置，每次复位
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:  # 注意位置，是在一次从头到尾比较完成之后
            break
    return arr


if __name__ == '__main__':
    test = [1, 4, 5, 3, -2, 10, 9]
    print bubble_sort(test)

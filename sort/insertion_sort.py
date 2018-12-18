# coding=utf-8


# 选择排序
def insertion_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    for i in range(1, length):
        # for j in range(0, i):  # 从前往后查找，一次性后移
        #     if arr[j] > arr[i]:
        #         tmp = arr[i]
        #         for k in range(i, j, -1):
        #             arr[k] = arr[k - 1]
        #         arr[j] = tmp
        #         break

        # value = arr[i]
        # for j in range(i - 1, -1, -1):  # 从后往前查找，逐步后移
        #     if arr[j] > value:
        #         arr[j + 1] = arr[j]
        #     else:
        #         break
        # else:
        #     j -= 1  # 之所以加上这句，是因为当j是因为循环到0才退出循环时，应该是arr[0]更新
        #     # for j in range(n) 和其它语言中的for(int j = 0; j < n; j++)是有区别的，结束循环时j的值不同

        # 更清晰的表达方式是使用while循环
        if arr[i] < arr[i - 1]:  # 如果待插入元素大则不需要排序
            value = arr[i]
            j = i - 1
            while j >= 0 and value < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = value
    return arr


# 带哨兵的优化，少了越界判断
def insertion_sort_opti(arr):
    length = len(arr)
    if length <= 1:
        return arr
    arr = [0] + arr[:]  # 在开头添加一个元素作为哨兵，暂存待插入元素，同时可以作为边界
    for i in range(2, length):
        if arr[i] < arr[i - 1]:  # 如果待插入元素大则不需要排序
            arr[0] = arr[i]
            j = i - 1
            while arr[0] < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = arr[0]
    return arr[1:]


if __name__ == '__main__':
    test = [1, 4, 5, 3, -2, 10, 9]
    # print insertion_sort(test)
    print insertion_sort_opti(test)
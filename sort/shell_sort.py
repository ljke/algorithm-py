# coding=utf-8


# 希尔排序
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = arr[i]
            j = i
            # 插入排序
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # 得到新的步长
        gap = gap // 2
    return arr


if __name__ == '__main__':
    test = [1, 4, 5, 3, -2, 10, 9]
    print shell_sort(test)

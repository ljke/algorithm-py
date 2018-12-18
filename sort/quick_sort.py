# coding=utf-8

# 快速排序
# 选取基准值，根据与基准值的大小关系对数据分区
# 递归调用，对分区也进行快速排序


# 非原地快排
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# 原地快排
def quick_sort_opti(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        i = 0
        for j in range(len(arr) - 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]  # 交换元素
                i += 1
        arr[i], arr[-1] = arr[-1], arr[i]
        return quick_sort_opti(arr[0:i]) + [pivot] + quick_sort_opti(arr[i+1:])


if __name__ == '__main__':
    test = [1, 4, 5, 3, -2, 10, 9]
    print quick_sort(test)
    test = [1, 4, 5, 3, -2, 10, 9]
    print quick_sort_opti(test)

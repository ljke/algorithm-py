# coding=utf-8

# 归并排序：分为递归法和迭代法，此处是递归法
# 基线条件：当前只有1个数据
# 递归：将左右两边都排好序
# 因为多了merge的操作，所以时间上不如快速排序


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


# 使用哨兵简化编程
def merge_opti(left, right):
    result = []
    length = len(left) + len(right)
    left.append(100)
    right.append(100)
    for i in range(length): #
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result


def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    # return merge(left, right)
    return merge_opti(left, right)


if __name__ == '__main__':
    test = [1, 4, 5, 3, -2, 10, 9]
    print merge_sort(test)
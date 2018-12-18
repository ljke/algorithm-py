# coding=utf-8


# 二分查找，针对有序序列，时间复杂度为O(log n)
# 核心思想是靠猜，猜中间的数字，可以排除一半的数据
def binary_search(cur_list, item):
    low = 0
    high = len(cur_list) - 1
    while low <= high:
        # mid = (low + high) / 2
        # 改进写法：减法避免溢出，位操作提高速度
        mid = low + ((high - low) >> 1)
        guess = cur_list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


# 递归版本的二分查找
def binary_search_recursive(cur_list, item, low, high):
    if low > high:
        return None
    mid = low + ((high - low) >> 1)
    guess = cur_list[mid]
    if guess == item:
        return mid
    elif guess < item:
        return binary_search_recursive(cur_list, item, mid + 1, high)
    else:
        return binary_search_recursive(cur_list, item, low, mid - 1)


# 二分查找法求平方根, 另一种求解平方根的方法是牛顿迭代法，参见math_algo.newton_method
def sqrt_bsearch(value):
    if value < 0:
        return None
    elif 1 > value > 0:  # 考虑小于0的情况，取值范围不同
        low = value
        high = 1
    else:
        low = 0.0
        high = value * 1.0
    mid = low + (high - low) / 2
    count = 1
    while abs(mid ** 2 - value) > 0.000001:
        print count, mid
        count += 1
        if mid ** 2 > value:
            high = mid
        else:
            low = mid
        mid = low + (high - low) / 2
    return mid


# 二分查找的变形

# 查找第一个等于给定值的元素，返回索引值
def bsearch_first_equal(cur_list, item):
    low = 0
    high = len(cur_list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        guess = cur_list[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            if mid == 0 or cur_list[mid - 1] != item:
                return mid
            else:
                high = mid - 1
    return None


# 查找最后一个等于给定值的元素，返回索引值
def bsearch_last_equal(cur_list, item):
    low = 0
    high = len(cur_list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        guess = cur_list[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            if mid == (len(cur_list) - 1) or cur_list[mid + 1] != item:
                return mid
            else:
                low = mid + 1
    return None


# 查找第一个大于等于给定值的元素，返回索引值
def bsearch_first_greater(cur_list, item):
    low = 0
    high = len(cur_list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        guess = cur_list[mid]
        if guess < item:
            low = mid + 1
        else:
            if mid == 0 or cur_list[mid - 1] < item:
                return mid
            else:
                high = mid - 1
    return None


# 查找最后一个小于等于给定值的元素，返回索引值
def bsearch_last_smaller(cur_list, item):
    low = 0
    high = len(cur_list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        guess = cur_list[mid]
        if guess > item:
            high = mid - 1
        else:
            if mid == (len(cur_list) - 1) or cur_list[mid + 1] > item:
                return mid
            else:
                low = mid + 1
    return None


# 查找某数所在范围：分为两次查找，分别查找左端和右端, 不存在返回(-1, -1)
def bsearch_range(cur_list, item):
    left = bsearch_first_equal(cur_list, item)
    if left is None:
        return -1, -1
    else:
        right = bsearch_last_equal(cur_list[left:], item) + left  # 从left右侧开始查找
        return left, right


# 查找两个数组中的第k个数
def bsearch_findKth(list1, list2, k):
    m = len(list1)
    n = len(list2)
    if m > n:  # always assume that m is equal or smaller than n
        return bsearch_findKth(list2, list1, k)
    if m == 0:  # 回归条件：一个数组为空，直接在另一个数组中查找即可
        return list2[k - 1]
    if k == 1:  # 回归条件：查找第一个数，比较两个数组第一个元素
        return min(list1[0], list2[0])
    pa = min(m, k / 2)  # 中值mid
    pb = k - pa
    # 递归，可以排除两个数组中较小的半部分，较小的半部分一定在第k个数前面，不然凑不够k个数
    if list1[pa - 1] < list2[pb - 1]:
        return bsearch_findKth(list1[pa:], list2, k - pa)
    elif list1[pa - 1] > list2[pb - 1]:
        return bsearch_findKth(list1, list2[pb:], k - pb)
    else:
        return list1[pa - 1]


# 寻找两个有序数组的中位数
def bsearch_median_of_two_array(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    total = length1 + length2
    if total % 2 == 1:  # 总个数是奇数
        return bsearch_findKth(list1, list2, total / 2 + 1)
    else:  # 总个数是偶数
        return (bsearch_findKth(list1, list2, total / 2) +
                bsearch_findKth(list1, list2, total / 2 + 1)) / 2


# 循环有序数组的二分查找
def bsearch_rotated_array(cur_list, item):
    low = 0
    high = len(cur_list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if cur_list[mid] == item:
            return mid
        # 注意：如果含有重复值，等于情况下无法判断，同时返回的只是其中一个值
        if cur_list[low] <= cur_list[mid]:  # 转折点在右半部分，在左半部分判断
            if cur_list[low] <= item < cur_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # 转折点在左半部分，在右半部分判断
            if cur_list[mid] < item <= cur_list[high]:
                low = mid + 1
            else:
                high = mid - 1
    return None


if __name__ == '__main__':
    # my_list = [1, 3, 5, 7, 9, 11]
    # print binary_search(my_list, 9)
    # print binary_search_recursive(my_list, 9, 0, len(my_list) - 1)
    # print sqrt(0.5)
    # print sqrt_bsearch(0.5)

    # my_list = [1, 3, 3, 3, 5, 7, 9, 11]
    # print bsearch_first_equal(my_list, 3)
    # print bsearch_last_equal(my_list, 3)
    # print bsearch_first_greater(my_list, 5)
    # print bsearch_last_smaller(my_list, 7)
    # print bsearch_range(my_list, 3)
    # print bsearch_range(my_list, 5)
    # print bsearch_range(my_list, 12)

    # my_list2 = [1, 2, 3, 5, 6, 8, 10, 13]
    # print bsearch_median_of_two_array(my_list, my_list2)

    my_list = [10, 14, 3, 4, 5, 9]
    print bsearch_rotated_array(my_list, 14)
    print bsearch_rotated_array(my_list, 9)

# coding=utf-8


# 计数排序
def counting_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    max_value = max(arr)
    min_value = min(arr)
    # 将数据最小值归一化为0
    offset = min_value
    arr = map(lambda x: x - offset, arr)
    max_value -= offset
    # 计算取值范围
    value_range = max_value + 1
    # 初始化计数数组
    c = [0] * value_range
    # 计数
    for i in range(length):
        c[arr[i]] += 1
    # 依次累加
    for i in range(1, value_range):
        c[i] = c[i - 1] + c[i]
    # 初始化结果数组
    r = [0] * length
    # 遍历原始数组，填充到结果数组的特定位置
    for i in reversed(range(length)):
        index = c[arr[i]] - 1
        r[index] = arr[i]
        c[arr[i]] -= 1
    # 返回原始数据
    return map(lambda x: x + offset, r)


if __name__ == '__main__':
    test = [1, 4, 5, 3, -2, 10, 9]
    print counting_sort(test)

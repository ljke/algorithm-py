# coding=utf-8


# 荷兰国旗问题,0,1,2分别表示三种颜色，使用前后指针分区和数据交换完成
# 时间复杂度O(n), 空间复杂度O(1)
def sort_color(arr):
    length = len(arr)
    if length <= 1:
        return arr
    begin = cur = 0
    end = length - 1
    while cur <= end:
        if arr[cur] == 0:
            arr[cur], arr[begin] = arr[begin], arr[cur]
            # 交换过来的数据必然是已经检查过的数据，除非cur = begin，否则交换过来的数据是1
            cur += 1
            begin += 1
        elif arr[cur] == 1:
            cur += 1
        elif arr[cur] == 2:
            arr[cur], arr[end] = arr[end], arr[cur]
            # 这里交换过来的数据可能属于前部，所以cur不加一，下次循环继续判断
            # cur += 1
            end -= 1
        else:
            raise Exception("Error Num")
    return arr


if __name__ == '__main__':
    test = [0, 2, 1, 0, 0, 1, 2]
    print sort_color(test)

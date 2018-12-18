# coding=utf-8

# 选择排序：每次都从中选择一个，直到选完，时间复杂度为O(n2)


def find_smallest(cur_arr):
    smallest_element = cur_arr[0]
    smallest_index = 0
    for i in range(1, len(cur_arr)):
        if cur_arr[i] < smallest_element:
            smallest_element = cur_arr[i]
            smallest_index = i
    return smallest_index


# 非原地排序但是稳定
def selection_sort(arr):
    sorted_arr = []
    for i in range(0, len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


# 原地排序但是不稳定
def selection_sort_opti(arr):
    for i in range(0, len(arr)):
        smallest = find_smallest(arr[i:])
        arr[i], arr[smallest + i] = arr[smallest + i], arr[i]
    return arr


if __name__ == '__main__':
    test = [1, 4, 5, 3, -2, 10, 9]
    print selection_sort(test)
    test = [1, 4, 5, 3, -2, 10, 9]
    print selection_sort_opti(test)

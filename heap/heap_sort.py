from heap import MaxHeap, MinHeap


def heap_sort(direction=True, nums=None):
    """
    :param direction: True means sort from small to large, False means sort from large to small
    :param nums: heap data
    :return: sorted data
    """
    # different direction correspond different heap type
    if direction:
        heap = MaxHeap(nums)
    else:
        heap = MinHeap(nums)
    return heap.sort()


if __name__ == '__main__':
    nums = [3, 5, 2, 6, 1, 7, 6]
    print '---increment sort---'
    print heap_sort(True, nums)

    print '---decrement sort---'
    print heap_sort(False, nums)

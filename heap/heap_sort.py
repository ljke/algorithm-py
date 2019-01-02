from heap import Heap


class SortedHeap(Heap):
    def __init__(self, nums=None, capacity=100):
        Heap.__init__(self, nums, capacity)

    def heap_sort(self):
        self.build_heap()
        data = self._data
        assert type(data) is list
        length = len(data)
        if length <= 1:
            return
        for i in range(length - 1, 0, -1):
            data[0], data[i] = data[i], data[0]
            self._heap_down(data, 0, i - 1)


if __name__ == '__main__':
    nums = [3, 5, 2, 6, 1, 7, 6]
    sh = SortedHeap(nums)
    print '---before sort---'
    print sh
    print '---after  sort---'
    sh.heap_sort()
    print sh

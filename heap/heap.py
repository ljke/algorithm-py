import math
import random


# Problem: Generic subclass can not be inherited, so unable to use
# from typing import TypeVar, Generic, List
# T = TypeVar("T")

class Heap:
    def __init__(self, nums=None, capacity=100):
        self._data = []
        self._capacity = capacity
        if type(nums) is list:
            if len(nums) > self._capacity:
                raise Exception('Heap oversize, capacity:{}, data size:{}'.format(self._capacity, len(nums)))
            # data start at 0 index
            for n in nums:
                assert type(n) is int
                self._data.append(n)
        self._length = len(self._data)

    def get_data(self):
        return self._data

    def get_length(self):
        return self._length

    def _heap_down(self, data, idx, tail_idx):
        pass

    def _heap_up(self, data, idx):
        pass

    def build_heap(self):
        """
        build heap from data
        :return:
        """
        data = self._data
        tail_idx = self._length - 1
        if tail_idx <= 0:
            return
        # index of the last parent node
        lp = (tail_idx - 1) // 2
        for i in range(lp, -1, -1):  # begin from last parent node
            self._heap_down(data, i, tail_idx)

    def insert(self, num):
        if self._length < self._capacity:
            if self._insert(self._data, num):
                self._length += 1
                return True
        return False

    def _insert(self, data, num):
        assert type(data) is list
        assert type(num) is int
        data.append(num)
        length = len(data)
        # index of new node
        nn = length - 1
        # heapify from bottom to up
        self._heap_up(data, nn)
        return True

    def get_top(self):
        if self._length <= 0:
            return None
        return self._data[0]

    def remove_top(self):
        ret = None
        if self._length > 0:
            ret = self._remove_top(self._data)
            self._length -= 1
        return ret

    def _remove_top(self, data):
        assert type(data) is list
        length = len(data)
        if length == 0:
            return None
        data[0], data[-1] = data[-1], data[0]
        ret = data.pop()
        length -= 1
        if length > 1:
            self._heap_down(data, 0, length - 1)
        return ret

    def sort(self):
        """
        :return: None if data is empty, else, return sorted data
        """
        data = self._data
        assert type(data) is list
        length = len(data)
        if length <= 1:
            return None
        self.build_heap()
        for i in range(length - 1, 0, -1):
            data[0], data[i] = data[i], data[0]  # swap to tail
            self._heap_down(data, 0, i - 1)
        return self._data

    @staticmethod
    def _draw_heap(data):
        length = len(data)
        if length == 0:
            return 'empty heap'
        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            if i == 2 ** int(math.log(i + 1, 2) + 1) - 2 or i == len(data) - 1:  # Equal ratio series summation formula
                ret += '\n'
            else:
                ret += ','
        return ret

    def __repr__(self):
        return self._draw_heap(self._data)


class MaxHeap(Heap):
    def _heap_down(self, data, idx, tail_idx):
        """
        heapify from top to bottom
        :param data: source array
        :param idx:start node index
        :param tail_idx:end node index
        """
        assert type(data) is list
        lp = (tail_idx - 1) // 2
        # top-down
        while idx <= lp:
            # left and right child index
            lc = 2 * idx + 1
            rc = lc + 1
            # get the maximum between two children
            if rc <= tail_idx:
                tmp = lc if data[lc] > data[rc] else rc
            else:
                tmp = lc
            # get the maximum between parent and children
            if data[tmp] > data[idx]:
                data[tmp], data[idx] = data[idx], data[tmp]
                idx = tmp
            else:
                break  # do not need to swap, heapify finished, exit early

    def _heap_up(self, data, idx):
        """
        heapify from bottom to top
        :param data: source array
        :param idx: heapify node index
        """
        assert type(data) is list
        while idx > 0:
            p = (idx - 1) // 2  # parent node
            # compare with parent node
            if data[idx] > data[p]:
                data[idx], data[p] = data[p], data[idx]
                idx = p
            else:
                break


class MinHeap(Heap):
    def _heap_down(self, data, idx, tail_idx):
        """
        heapify from top to bottom
        :param data: source array
        :param idx:start node index
        :param tail_idx:end node index
        """
        assert type(data) is list
        lp = (tail_idx - 1) // 2
        # top-down
        while idx <= lp:
            # left and right child index
            lc = 2 * idx + 1
            rc = lc + 1
            # get the minimum between two children
            if rc <= tail_idx:
                tmp = lc if data[lc] < data[rc] else rc
            else:
                tmp = lc
            # get the minimum between parent and children
            if data[tmp] < data[idx]:
                data[tmp], data[idx] = data[idx], data[tmp]
                idx = tmp
            else:
                break  # do not need to swap, heapify finished, exit early

    def _heap_up(self, data, idx):
        """
        heapify from bottom to top
        :param data: source array
        :param idx: heapify node index
        """
        assert type(data) is list
        while idx > 0:
            p = (idx - 1) // 2  # parent node
            # compare with parent node
            if data[idx] < data[p]:
                data[idx], data[p] = data[p], data[idx]
                idx = p
            else:
                break


if __name__ == '__main__':
    nums = list(range(10))
    random.shuffle(nums)
    print 'Max Heap:'
    bh = MaxHeap(nums)
    print '---before build heap---'
    print bh
    print '---after build heap---'
    bh.build_heap()
    print bh
    print '---insert heap---'
    if bh.insert(8):
        print 'insert success'
    else:
        print 'insert fail'
    print bh
    # get top
    print '---get top---'
    print 'get top of the heap:{}'.format(bh.get_top())
    bh.remove_top()
    print bh

    random.shuffle(nums)
    print 'Min Heap:'
    bh = MinHeap(nums)
    print '---before build heap---'
    print bh
    print '---after build heap---'
    bh.build_heap()
    print bh
    print '---insert heap---'
    if bh.insert(8):
        print 'insert success'
    else:
        print 'insert fail'
    print bh
    # get top
    print '---get top---'
    print 'get top of the heap:{}'.format(bh.get_top())
    bh.remove_top()
    print bh

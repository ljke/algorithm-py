import random

from heap import MinHeap


def get_static_top_k(nums, k):
    """
    get top-K of static data
    :param nums:
    :param k:
    :return:
    """
    if len(nums) <= k:
        return nums
    min_h = MinHeap(nums[:k], k)  # one time use
    min_h.build_heap()
    # compare data with heap top
    for n in range(k, len(nums)):
        tmp = min_h.get_top()
        if nums[n] > tmp:  # if larger, change data
            min_h.remove_top()
            min_h.insert(nums[n])
    return min_h.get_data()


# class TopK use to get top-K of dynamic data
class TopK:
    def __init__(self, k):
        self.k = k
        self.heap = MinHeap(capacity=k)

    def add_data(self, num):
        assert type(num) is int
        if self.heap.get_length() < self.k:
            self.heap.insert(num)
        else:
            tmp = self.heap.get_top()
            if num > tmp:  # if larger, change data
                self.heap.remove_top()
                self.heap.insert(num)

    def get_top_k(self):
        return 'current top-k is :' + str(self.heap.get_data())

    def __repr__(self):
        return self.heap.__repr__()


if __name__ == '__main__':
    nums = []
    k = 3
    for i in range(20):
        nums.append(random.randint(1, 100))
    print '--- nums ---'
    print nums
    print '--- top {} ---'.format(k)
    print get_static_top_k(nums, k)

    print '--- 0 ---'
    top_k = TopK(k)
    print top_k

    print '--- 1 ---'
    n = random.randint(1, 100)
    print 'add new node:', n
    top_k.add_data(n)
    print top_k
    print top_k.get_top_k()

    print '--- 2 ---'
    n = random.randint(1, 100)
    print 'add new node:', n
    top_k.add_data(n)
    print top_k
    print top_k.get_top_k()

    print '--- 3 ---'
    n = random.randint(1, 100)
    print 'add new node:', n
    top_k.add_data(n)
    print top_k
    print top_k.get_top_k()

    print '--- 4 ---'
    n = random.randint(1, 100)
    print 'add new node:', n
    top_k.add_data(n)
    print top_k
    print top_k.get_top_k()

    print '--- 5 ---'
    n = random.randint(1, 100)
    print 'add new node:', n
    top_k.add_data(n)
    print top_k
    print top_k.get_top_k()

# coding=utf-8
from itertools import chain


class CircularQueue:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity + 1  # 空闲一个位置
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if (self._tail + 1) % self._capacity == self._head:
            return False
        if self._tail == len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item;
        self._tail = (self._tail + 1) % self._capacity
        return True
        # append会一直添加元素，不符合要求
        # if (self._tail + 1) % self._capacity == self._head:
        #     return False
        #
        # self._items.append(item)
        # self._tail = (self._tail + 1) % self._capacity
        # return True

    def dequeue(self):
        if self._head == self._tail:
            return None
        else:
            ret = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return ret

    def __repr__(self):
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head:self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == '__main__':
    q = CircularQueue(5)
    for i in range(6):
        q.enqueue(str(i))
    for i in range(6):
        q.dequeue()
    for i in range(6):
        q.enqueue(str(i))
    print q
    q.dequeue()
    print q

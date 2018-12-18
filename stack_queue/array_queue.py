# coding=utf-8
class ArrayQueue:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if self._tail == self._capacity:  # 队尾到边界
            return False
        else:
            self._items.append(item)
            self._tail += 1
            return True

    def dequeue(self):
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self):
        return " ".join(item for item in self._items[self._head:self._tail])

# coding=utf-8
class DynamicArrayQueue:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                self._items[0:self._tail - self._head] = self._items[self._head:self._tail]
                self._tail -= self._head
                self._head = 0
        if self._tail == len(self._items):
            self._items.append(item)
        else:  # 需要特殊处理，因为可能是数据搬移后的，所以可能不需要开辟新空间
            self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self):
        if self._head == self._tail:
            return None
        else:
            item = self._items[self._head]
            self._head += 1
            return item

    def __repr__(self):
        return " ".join(item for item in self._items[self._head:self._tail])


if __name__ == '__main__':
    q = DynamicArrayQueue(10)
    for i in range(10):
        q.enqueue(str(10))
    print q

    for _ in range(3):
        q.dequeue()
    print q

    q.enqueue("7")
    q.enqueue("8")
    print q

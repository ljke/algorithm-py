class Node(object):
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node


class LinkedStack(object):
    _top = None  # type: Node

    def __init__(self):
        self._top = None

    def push(self, value):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top

    def pop(self):
        if self._top:
            value = self._top._data  # access Node's protected member
            self._top = self._top._next
            return value

    def __repr__(self):
        current = self._top  # type: Node
        nums = []  # copy to a list
        while current:
            nums.append(current._data)
            current = current._next
        return " ".join(str(num) for num in nums)  # 'join' require str


if __name__ == '__main__':
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print stack
    for _ in range(3):
        stack.pop()
    print stack

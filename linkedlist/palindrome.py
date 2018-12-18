# coding=utf-8
class Node(object):
    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.next = None


def create_linklist(string):
    head = Node(string[0])
    pre = head
    for i in string[1:]:
        new_node = Node(i)
        pre.next = new_node
        pre = new_node
    new_node.next = None
    return head


def is_palindrome(head):
    fast = slow = head
    while fast and fast.next:  # 注意遍历停止条件
        fast = fast.next.next
        slow = slow.next
    prev = None
    while slow:
        tmp = slow.next  # 1.暂存正向后继结点
        slow.next = prev  # 2. 指向正向前驱结点，完成反向
        prev = slow  # 3. 更新正向前驱结点，也就是反向的后继结点
        slow = tmp  # 4. 恢复当前结点为正向后继结点，继续往后遍历
    while prev:
        print prev.value, " compare ", head.value
        if prev.value != head.value:
            return False
        prev = prev.next
        head = head.next
    return True


# 奇数情况
#           None         fast     tmp
#            ^           prev     slow
#            |            ^        ^
#            |            |        |
# 1 --> 2 --> 3 <-- 2 <-- 1       None

# 偶数情况
#                           tmp
#           None            slow
#            ^     prev     fast
#            |      ^        ^
#            |      |        |
# 1 --> 2 --> 2 <-- 1       None

if __name__ == '__main__':
    string = raw_input("Input str:")
    head = create_linklist(string)
    print is_palindrome(head)

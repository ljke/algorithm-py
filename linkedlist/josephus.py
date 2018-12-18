# coding=utf-8

# 使用循环链表解决约瑟夫问题


class Node(object):
    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.next = None


def create_linklist(n):
    head = Node(1)
    pre = head
    for i in range(2, n + 1):
        new_node = Node(i)
        pre.next = new_node
        pre = new_node
    pre.next = head
    return head


if __name__ == '__main__':
    n = 5
    m = 2
    if m == 1:
        print n
    else:
        head = create_linklist(n)
        pre = None
        cur = head
        while cur.next != cur:  # 这个条件会剩下一个结点
            # 不断遍历
            for i in range(m - 1):
                pre = cur
                cur = cur.next
            print cur.value
            # 删除结点
            pre.next = cur.next
            cur.next = None
            cur = pre.next
        print "left:", cur.value

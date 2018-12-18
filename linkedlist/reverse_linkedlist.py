# coding=utf-8
class Node(object):
    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.next = None


def create_linked_list(nodelist):
    """
    :type nodelist: list
    """
    if (nodelist is not list) or (len(nodelist) < 1):
        return None
    else:
        head = Node(nodelist[0])
        pre = head
        for i in nodelist[1:]:
            new_node = Node(i)
            pre.next = new_node
            pre = new_node
        pre.next = None
        return head


def print_linked_list(head):
    # type: (Node) -> None
    while head:
        print "[", head.value, "]",
        head = head.next
    print ""


def reverse_linked_list(head):
    prev = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev


def reverse_linked_list_2(head):
    def helper(head, new_head):
        if head:
            nxt = head.next
            head.next = new_head
            return helper(nxt, head)
        else:
            return new_head
    return helper(head, None)


if __name__ == '__main__':
    node_list = [1, 2, 3, 4, 5, 6]
    linkedlist = create_linked_list(node_list)
    print_linked_list(linkedlist)
    # reversed = reverse_linked_list(linkedlist)
    reversed2 = reverse_linked_list_2(linkedlist)
    # print_linked_list(reversed)
    print_linked_list(reversed2)
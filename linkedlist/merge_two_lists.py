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


def merge_two_lists(l1, l2):
    # type: (Node, Node) -> Node
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    dummy = Node(-1)
    cur = dummy

    while l1 and l2:
        if l1.value < l2.value:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    if l1:
        cur.next = l1
    else:
        cur.next = l2

    return dummy.next


if __name__ == '__main__':
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    linkedlist1 = create_linked_list(list1)
    linkedlist2 = create_linked_list(list2)
    print_linked_list(linkedlist1)
    print_linked_list(linkedlist2)
    merged = merge_two_lists(linkedlist1, linkedlist2)
    print_linked_list(merged)

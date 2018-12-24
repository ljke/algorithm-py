import math
from Queue import Queue

from typing import Optional


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None  # store parent pointer in order to delete


class BinarySearchTree:
    def __init__(self, val_list=[]):
        self.root = None
        for n in val_list:
            self.insert(n)

    def insert(self, data):  # type: (int) -> bool
        """
        insert node into tree
        :param data:
        :return: True if succeed
        """
        assert (isinstance(data, int))
        if self.root is None:  # special situation: add root node
            self.root = TreeNode(data)
        else:
            n = self.root
            p = None
            while n:
                p = n
                if data < n.val:
                    n = n.left
                else:
                    n = n.right
            new_node = TreeNode(data)
            new_node.parent = p

            if data < p.val:
                p.left = new_node
            else:
                p.right = new_node

        return True

    def search(self, data):  # type: (int) -> list
        """
        search for all nodes of specified data
        :param data:
        :return: list of corresponding node
        """
        assert (isinstance(data, int))
        ret = []
        n = self.root
        while n:
            if data < n.val:
                n = n.left
            else:
                if data == n.val:
                    ret.append(n)
                n = n.right
        return ret

    def _del_node(self, node):  # type: (TreeNode) -> bool
        """
        delete single node that appoint
        :param node: appoint node
        :return: True if succeed
        """
        assert (isinstance(node, TreeNode))
        parent = node.parent
        # divide into three situation:
        # (1). node has two subtree
        if node.left and node.right:
            # find min of right subtree
            minPP = node
            minP = node.right
            while minP.left:
                minPP = minP
                minP = minP.left
            node.val = minP.val
            node = minP
            parent = minPP

        # (2). node has single subtree
        if node.left:
            child = node.left
        elif node.right:
            child = node.right
        else:
            child = None  # (3). node has no subtree

        if not parent:  # special situation: delete root node
            self.root = child
        # delete specified node
        elif parent.left == node:
            parent.left = child
        elif parent.right == node:
            parent.right = child
        else:
            return False  # delete failed

        return True

    def delete_first(self, data):  # type: (int) -> bool
        """
        delete first node that value equals data
        :param data:
        :return: True if succeed
        """
        nodes = self.search(data)
        if len(nodes):
            res = self._del_node(nodes[0])
        else:
            res = False
        return res

    def delete_all(self, data):  # type: (int) -> bool
        """
        delete all nodes that value equals data
        :param data:
        :return: True if succeed
        """
        nodes = self.search(data)
        res = True
        if len(nodes):
            for node in nodes:
                res = res & self._del_node(node)  # integrate every node's result
        else:
            res = False
        return res

    def get_min(self):
        # type: () -> Optional[int]
        if self.root is None:
            return None
        n = self.root
        while n.left:
            n = n.left
        return n.val

    def get_max(self):
        # type: () -> Optional[int]
        if self.root is None:
            return None
        n = self.root
        while n.right:
            n = n.right
        return n.val

    def in_order_sort(self):  # type: () -> list
        """
        in-order traversal to get sorted list of tree nodes
        :return:
        """
        if self.root is None:
            return []
        else:
            return self._in_order(self.root)

    def _in_order(self, node):  # type: (TreeNode) -> list
        if node is None:
            return []
        ret = []
        ret.extend(self._in_order(node.left))
        ret.append(node.val)
        ret.extend(self._in_order(node.right))
        return ret

    def __repr__(self):
        print str(self.in_order_sort())
        return self._draw_tree()

    def _bfs(self):  # type: () -> list
        """
        record (node, index) of every level
        :return: list of (node, index)
        """
        if self.root is None:
            return []
        ret = []
        q = Queue()
        q.put((self.root, 1))

        while not q.empty():
            n = q.get()

            if n[0] is not None:
                ret.append((n[0].val, n[1]))
                q.put((n[0].left, n[1] * 2))  # left child's index
                q.put((n[0].right, n[1] * 2 + 1))  # right child's index

        return ret

    def _draw_tree(self):
        nodes = self._bfs()
        if not nodes:
            print "Tree is empty"
            return
        layer_num = int(math.log(nodes[-1][1], 2)) + 1
        prt_nums = []  # a two-dimensional list store every layer of tree
        for i in range(layer_num):
            prt_nums.append([None] * 2 ** i)  # empty tree structure
        for v, p in nodes:
            # calculate node position
            row = int(math.log(p, 2))
            col = p % (2 ** row)
            prt_nums[row][col] = v
        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'  # [1, -1] to crop square brackets in every element
        return prt_str


if __name__ == '__main__':
    nums = [4, 2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    print(bst)
    # search
    for n in bst.search(2):
        print(n.parent.val, n.val)
    # delete
    bst.insert(6)
    bst.insert(7)
    print(bst)
    print "delete:" + str(bst.delete_first(7))
    print(bst)
    print "delete:" + str(bst.delete_all(6))
    print(bst)
    # min max
    print(bst.get_max())
    print(bst.get_min())

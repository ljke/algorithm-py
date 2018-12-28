from Queue import Queue

import pygraphviz as pgv

OUTPUT_PATH = './'


class TreeNode:
    def __init__(self, val=None, color=None):
        self.val = val
        assert color in ['r', 'b']
        self.color = 'red' if color == 'r' else 'black'
        self.left = None
        self.right = None
        self.parent = None

    def is_black(self):
        return self.color == 'black'

    def set_black(self):
        self.color = 'black'

    def set_red(self):
        self.color = 'red'


class RedBlackTree:
    def __init__(self, val_list=None):
        self.root = None
        self.black_leaf = TreeNode(color='b')  # shared black leaf node
        if type(val_list) is list:
            for n in val_list:
                assert type(n) is int
                self.insert(n)

    @staticmethod
    def bro(node):
        """
        get brother node
        :param node:
        :return:
        """
        if node is None or node.parent is None:
            return None
        else:
            p = node.parent
            if node == p.left:
                return p.right
            else:
                return p.left

    @staticmethod
    def parent(node):
        """
        get parent node
        :param node:
        :return:
        """
        if node is None:
            return None
        else:
            return node.parent

    def rotate_l(self, node):
        """
        left rotate of node
        :param node:
        :return:
        """
        if node is None:
            return
        if node.right is self.black_leaf:  # has no right child, can not rotate left
            return
        p = self.parent(node)
        x = node
        y = node.right
        # update parent
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:  # node is root node
            self.root = y
        # update x and y
        x.parent, y.parent = y, p
        if y.left != self.black_leaf:  # transplant subtree
            y.left.parent = x
        x.right, y.left = y.left, x

    # similar to left-rotate
    def rotate_r(self, node):
        """
        right rotate of node
        :param node:
        :return:
        """
        if node is None:
            return
        if node.left is self.black_leaf:
            return
        p = self.parent(node)
        x = node
        y = node.left
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y
        x.parent, y.parent = y, p
        if y.right != self.black_leaf:
            y.right.parent = x
        x.left, y.right = y.right, x

    def children_count(self, node):
        """
        count the leaf num in children of node
        :param node:
        :return:
        """
        return 2 - [node.left, node.right].count(self.black_leaf)

    def search(self, val):
        if self.root is None:
            return None
        n = self.root
        while n != self.black_leaf:
            if val < n.val:
                n = n.left
            elif val > n.val:
                n = n.right
            else:
                return n
        return None

    def insert(self, val):
        assert type(val) is int
        new_node = TreeNode(val, 'r')
        if self.root is None:
            # insert into root node
            self.root = new_node
        else:
            # find insert position in black leaf node
            n = self.root
            p = None
            while n != self.black_leaf:
                p = n
                if val < n.val:
                    n = n.left
                elif val > n.val:
                    n = n.right
                else:
                    raise KeyError('val:{} already exists')
            # insert new_node into proper leaf node
            if val < p.val:
                p.left = new_node
            else:
                p.right = new_node
            new_node.parent = p
        # add black leaf node
        new_node.left = new_node.right = self.black_leaf
        # adjustment
        self._insert_fixup(new_node)

    def _insert_fixup(self, node):
        n = node  # concern node
        # end condition: no longer need to adjust
        # 1. insert into root node
        # 2. parent is black
        while n is not self.root and not n.parent.is_black():
            # p-parent node, u-uncle node, g-grandparent
            p = self.parent(n)
            u = self.bro(p)
            g = self.parent(p)
            # CASE 1:
            if not u.is_black():
                p.set_black()
                u.set_black()
                g.set_red()
                n = g
                continue
            # divide into two cases: left child or right child, they are symmetry
            if p == g.left:  # parent is grandparent's left child
                # CASE 2:
                if n == p.right:
                    self.rotate_l(p)
                    n, p = p, n  # change concern node
                # CASE 3:
                p.set_black()
                g.set_red()
                self.rotate_r(g)
            else:  # parent is grandparent's right child
                # CASE 2:
                if n == p.left:
                    self.rotate_r(p)
                    n, p = p, n  # change concern node
                # CASE 3:
                p.set_black()
                g.set_red()
                self.rotate_l(g)
        # set root color to black
        # root may be red in two condition:
        # 1. insert into root node
        # 2. CASE 1 adjustment
        self.root.set_black()

    def delete(self, val):
        assert type(val) is int
        n = self.search(val)  # n is deleted node
        if n is None:
            print 'can not find any node equal to value: {}'.format(val)
            return
        # First stage adjustment for deleted node
        if self.children_count(n) == 2:  # have two no-nil child node
            # find 'next' node
            s = n.right
            while s.left != self.black_leaf:
                s = s.left
            n.val = s.val  # replace value
            n = s  # change deleted node
            # Note: s must have less than two no-nil child node
        # have one no-nil child node
        if n.left == self.black_leaf:
            c = n.right  # c is concern node
        else:
            c = n.left
        self._transplant(n, c)
        # Second stage adjustment for concern node
        # if delete black node, need to fixup
        if n.is_black():
            self._delete_fixup(c)

    def _transplant(self, n1, n2):
        """
        node transplant, n2 -> n1
        :param n1:
        :param n2:
        """
        if n1 == self.root:  # transplant to root node
            if n2 != self.black_leaf:
                self.root = n2
                n2.parent = None
            else:
                self.root = None  # delete root node
        else:
            p = self.parent(n1)
            if p.left == n1:
                p.left = n2
            else:
                p.right = n2
            n2.parent = p

    def _delete_fixup(self, node):
        n = node  # concern node
        while n is not self.root and n.is_black():
            p = self.parent(n)
            b = self.bro(n)
            # divide into two cases: node is left child or right child, they are symmetry
            if p.left == n:
                # CASE 1:
                if not b.is_black():
                    b.set_black()
                    p.set_red()
                    self.rotate_l(p)
                    # p will no changed, but b will change, and b is used for decision, so it needs update
                    b = self.bro(n)
                # CASE 2:
                if b.left.is_black() and b.right.is_black():
                    b.set_red()
                    n = p
                else:
                    # CASE 3:
                    if b.right.is_black():
                        b.left.set_black()
                        b.set_red()
                        self.rotate_r(b)
                        # new bro after rotate
                        b = self.bro(n)
                    # CASE 4:
                    # because p may be red or black, you cannot assign colors directly, you can only copy
                    b.color = p.color
                    p.set_black()
                    b.right.set_black()
                    self.rotate_l(p)
                    # trick, end while
                    n = self.root
            else:
                # CASE 1:
                if not b.is_black():
                    b.set_black()
                    p.set_red()
                    self.rotate_r(p)
                    # new bro after rotate
                    b = self.bro(n)
                # CASE 2:
                if b.left.is_black() and b.right.is_black():
                    b.set_red()
                    n = p
                else:
                    # CASE 3:
                    if b.left.is_black():
                        b.right.set_black()
                        b.set_red()
                        self.rotate_l(b)
                        # new bro after rotate
                        b = self.bro(n)

                    # CASE 4:
                    # because p may be red or black, you cannot assign colors directly, you can only copy
                    b.color = p.color
                    p.set_black()
                    b.left.set_black()
                    self.rotate_r(p)
                    # trick, end while
                    n = self.root  # case 4
        # set n black color
        # 1. n is root node, ignored
        # 2. n is red node, change color
        n.set_black()

    def draw_img(self, img_name='Red_Black_Tree.png'):
        """
        draw tree structure used pygraphviz
        :param img_name:
        :return:
        """
        if self.root is None:
            return
        tree = pgv.AGraph(directed=True, strict=True)
        q = Queue()
        q.put(self.root)

        while not q.empty():
            n = q.get()
            if n != self.black_leaf:
                tree.add_node(n.val, color=n.color)
                for c in [n.left, n.right]:  # black leaf node will also be added into queue
                    q.put(c)
                    color = 'red' if c == n.left else 'black'  # left and right use different color
                    if c != self.black_leaf:
                        tree.add_edge(n.val, c.val, color=color)
                    else:  # black leaf node will also be drew
                        tree.add_edge(n.val, 'None', color=color)
        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw(OUTPUT_PATH + img_name)
        return True


if __name__ == '__main__':
    rbt = RedBlackTree()
    # insert
    nums = list(range(1, 10))
    for num in nums:
        rbt.insert(num)
    # draw image
    rbt.draw_img('rbt1.png')
    # search
    search_num = 4
    n = rbt.search(search_num)
    if n is not None:
        print n.val
    else:
        print 'node {} not found'.format(search_num)
    # delete
    rbt.delete(4)
    # draw image
    rbt.draw_img('rbt2.png')
    # insert
    rbt.insert(4)
    # draw image
    rbt.draw_img('rbt3.png')

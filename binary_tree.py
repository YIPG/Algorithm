# 1. 二分木

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.h = 0

    # 2.Delete

    def _findMin(node):
        if node.l == None:
            return node.v
        else:
            return Node._findMin(node.l)

    def _deleteMin(node):
        if node.l == None:
            return node.r
        else:
            node.l = Node._deleteMin(node.l)
            return node

    def delete(node, val):
        if node:
            if val == node.v:
                if node.l is None:
                    return node.r
                elif node.r is None:
                    return node.l
                else:
                    node.v = Node._findMin(node.r)
                    node.r = Node._deleteMin(node.r)
            elif val < node.v:
                node.l = Node.delete(node.l, val)
            else:
                node.r = Node.delete(node.r, val)
        return node

    # 3. rotate

    # def get_height(node):
    #     if node == None:
    #         return 0
    #     else:
    #         Node.node._get_height(node,0)
    #
    # def _get_height(node,height):
    #     if node == None:
    #         return height
    #     l_height = Node._get_balance(node.l, height + 1)
    #     r_height = Node._get_balance(node.r, height + 1)
    #     return max(l_height, r_height)
    #
    # def rotate_left(node):
    #     rnode = node.r
    #     node.r = rnode.l
    #     rnode.l = node
    #     return rnode
    #
    # def rotate_right(node):
    #     lnode = node.l
    #     node.l = lnode.r
    #     lnode.r = node
    #     return lnode


class Tree:
    def __init__(self):
        self.root = None

    def add_list(self, l):
        for i in l:
            self.add(i)

    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):  # Private Function
        if val == node.v:
            print("Already existed in tree!")
        if (val < node.v):
            if (node.l == None):
                node.l = Node(val)
            else:
                self._add(val, node.l)
        else:
            if (node.r == None):
                node.r = Node(val)
            else:
                self._add(val, node.r)


    def find(self, val):
        if self.root != None:
            return self._find(val, self.root)
        else:
            return False


    def _find(self, val, node):
        if node == None:
            return False
        if val == node.v:
            return True
        elif val > node.v:
            return self._find(val, node.r)
        elif val < node.v:
            return self._find(val, node.l)

    def printtree(self):
        if self.root == None:
            print("Tree doesn't exist yet!")
        else:
            self._printtree(self.root)

    def _printtree(self, node):
        try:
            self._printtree(node.l)
            print(str(node.v))
            self._printtree(node.r)
        except:
            return None

# 2.Delete
#
# はじめに探索して対象のノードを探す。 その後、子の有無によって処理を分ける。
#
# 1 子がない場合 ~~ 対象のノードは葉であるので、node.v == NoneでOK
# 2 一つの子がある場合 ~~ node = 存在する方の子(node.r or node.l)にすればOK
# 3 どちらの子もある場合 ~~ 右の子から最小の値(node.min)を探し、node.v = node._findMinとする。のちに、
#   最小の値を持つnode_minをnode_min = node.rとすればOK.
#


    def delete(self, val):
        if self.root == None:
            print("Tree doesn't exist!")
        else:
            self.root = Node.delete(self.root, val)

# 3. 計算量: O(logn)
# 探索の操作が最悪なのは, [1,2,3,4,5...]のようにすでにソートされた配列を入れるとき。
# この場合計算量はO(n)となる。
# 木の高さを最高でlog_2(n)+1になるようにすれば, 計算量はO(logn)に抑えられる。

    #
    # def rotate(self):
    #     if self.root == None:
    #         print("Tree doesn't exist!")
    #     else:
    #         self.root = Node.rotate(self.root)


# Test
# ________


import random

if __name__ == "__main__":
    tree = Tree()

    random.seed(0)
    l = [random.randint(1, 100) for x in range(10)]

    print(l)

    tree.add_list(l)

    tree.printtree()

    print(tree.find(50))

    for i in l:
        tree.delete(i)

    print(tree.find(50))

    tree.printtree()

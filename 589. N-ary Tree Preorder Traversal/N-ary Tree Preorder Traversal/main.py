# -*- coding: utf-8 -*-

# Given an n-ary tree, return the preorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:

# Return its preorder traversal as: [1,3,5,6,2,4].

# Note:
#
# Recursive solution is trivial, could you do it iteratively?


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    # def __init__(self):
        # self.r_list = []

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # if root is None:
        #     return None
        #
        # self.r_list.append(root.val)
        #
        # if root.children is None:
        #     return None
        #
        # for node in root.children:
        #     self.preorder(node)
        #
        # return self.r_list

        return self.custom_preorder(root, [])

    def custom_preorder(self, root, A):
        """
        :type root: Node
        :type A: List[int]
        :rtype: List[int]
        """
        if root is None:
            return A

        A.append(root.val)

        if root.children is None:
            return A

        for node in root.children:
            self.custom_preorder(node, A)

        return A


if __name__ == '__main__':

    node5 = Node(5, None)
    node6 = Node(6, None)
    node3 = Node(3, [node5, node6])
    node2 = Node(2, None)
    node4 = Node(4, None)
    node1 = Node(1, [node3, node2, node4])

    solution = Solution()
    r_list = solution.preorder(node1)

    print r_list
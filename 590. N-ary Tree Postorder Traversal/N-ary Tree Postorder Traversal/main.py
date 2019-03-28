# -*- coding: utf-8 -*-

# Given an n-ary tree, return the postorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:
#
# Return its postorder traversal as: [5,6,3,2,4,1].
#
# Note:
#
# Recursive solution is trivial, could you do it iteratively?


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if root is None:
            return []

        A = []
        if root.children is not None:
            for node in root.children:
                a = self.postorder(node)
                A += a if a is not None else None

        A.append(root.val)
        return A


if __name__ == '__main__':

    node5 = Node(5, None)
    node6 = Node(6, None)
    node3 = Node(3, [node5, node6])
    node2 = Node(2, None)
    node4 = Node(4, None)
    node1 = Node(1, [node3, node2, node4])

    solution = Solution()
    r_list = solution.postorder(node1)

    print r_list

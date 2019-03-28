# -*- coding: utf-8 -*-

# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# For example, given a 3-ary tree:

# We should return its max depth, which is 3.

# Note:
#
# 1. The depth of the tree is at most 1000.
# 2. The total number of nodes is at most 5000.


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0

        if not root.children:
            return 1

        return 1 + max(self.maxDepth(a) for a in root.children)


if __name__ == '__main__':
    node5 = Node(5, None)
    node6 = Node(6, None)
    node3 = Node(3, [node5, node6])
    node2 = Node(2, None)
    node4 = Node(4, None)
    node1 = Node(1, [node3, node2, node4])

    solution = Solution()
    result = solution.maxDepth(node1)
    print 'result --- %d' % result
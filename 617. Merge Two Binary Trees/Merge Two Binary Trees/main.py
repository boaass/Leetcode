# -*- coding:utf-8 -*-

# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees
# are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up
#  as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# Example 1:
#
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

    def printNode(self, t):
        """
        :type t: TreeNode
        """
        if t is not None:
            print t.val
            self.printNode(t.left)
            self.printNode(t.right)


if __name__ == '__main__':
    t12 = TreeNode(2)
    t12.left = None
    t12.right = None

    t15 = TreeNode(5)
    t15.left = None
    t15.right = None

    t13 = TreeNode(3)
    t13.left = t15
    t13.right = None

    t11 = TreeNode(1)
    t11.left = t13
    t11.right = t12

    t24 = TreeNode(4)
    t24.left = None
    t24.right = None

    t27 = TreeNode(7)
    t27.left = None
    t27.right = None

    t21 = TreeNode(1)
    t21.left = None
    t21.right = t24

    t23 = TreeNode(3)
    t23.left = None
    t23.right = t27

    t22 = TreeNode(2)
    t22.left = t21
    t22.right = t23

    solution = Solution()
    result_node = solution.mergeTrees(t11, t22)

    solution.printNode(result_node)

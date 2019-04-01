# -*- coding: utf-8 -*-

# Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
# and every node has no left child and only 1 right child.
#
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
#
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \
# 1        7   9
#
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9
# Note:
#
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        vals = []
        self.inorder(root, vals)

        node_f = node_a = TreeNode(vals[0])

        for index in xrange(1, len(vals)):

            node_a.right = TreeNode(vals[index])
            node_a = node_a.right

        return node_f

    def inorder(self, node, vals):
        """
        中序遍历
        :param node: TreeNode
        :param vals: List<int>
        """

        if node is None:
            return None

        self.inorder(node.left, vals)
        vals.append(node.val)
        self.inorder(node.right, vals)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node1.left = None
    node1.right = None

    node7 = TreeNode(7)
    node7.left = None
    node7.right = None

    node9 = TreeNode(9)
    node9.left = None
    node9.right = None

    node2 = TreeNode(2)
    node2.left = node1
    node2.right = None

    node4 = TreeNode(4)
    node4.left = None
    node4.right = None

    node8 = TreeNode(8)
    node8.left = node7
    node8.right = node9

    node6 = TreeNode(6)
    node6.left = None
    node6.right = node8

    node3 = TreeNode(3)
    node3.left = node2
    node3.right = node4

    node5 = TreeNode(5)
    node5.left = node3
    node5.right = node6

    solution = Solution()
    bst = solution.increasingBST(node5)

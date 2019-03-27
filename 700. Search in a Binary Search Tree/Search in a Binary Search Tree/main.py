# -*- coding: utf-8 -*-

# Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's
# value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should
# return NULL.
#
# For example,
#
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# And the value to search: 2
# You should return this subtree:
#
#       2
#      / \
#     1   3
# In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.
#
# Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree
# format) as [], not null.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if root is None:
            return None

        if root.val == val:
            return root
        else:
            node_l = self.searchBST(root.left, val)
            if node_l is not None:
                return node_l
            else:
                node_r = self.searchBST(root.right, val)
                if node_r is not None:
                    return node_r

            return None


if __name__ == '__main__':

    node1 = TreeNode(1)
    node1.left = None
    node1.right = None

    node3 = TreeNode(3)
    node3.left = None
    node3.right = None

    node2 = TreeNode(2)
    node2.left = node1
    node2.right = node3

    node7 = TreeNode(2)
    node7.left = None
    node7.right = None

    node4 = TreeNode(4)
    node4.left = node2
    node4.right = node7

    solution = Solution()
    r_node = solution.searchBST(node4, 2)


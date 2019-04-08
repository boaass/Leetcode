# -*- coding:utf-8 -*-

# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements
#  lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root
# of the trimmed binary search tree.
#
# Example 1:
# Input:
#     1
#    / \
#   0   2
#
#   L = 1
#   R = 2
#
# Output:
#     1
#       \
#        2
# Example 2:
# Input:
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# Output:
#       3
#      /
#    2
#   /
#  1


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        if not root:
            return root

        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root


def createBTree(A):
    """
    :type A: list<Int>
    """
    if len(A) == 0:
        return None

    root = TreeNode(A[0])
    nodes = [root]

    index = 0
    while len(nodes) > 0 and index < len(A) - 2:
        node = nodes.pop(0)

        index += 1
        node.left = TreeNode(A[index])
        nodes.append(node)

        index += 1
        node.right = TreeNode(A[index])
        nodes.append(node)

    return root


def traverseBTree(root):
    """
    :type root: TreeNode 
    :return: None
    """

    if root is None:
        return

    traverseBTree(root.left)
    print root.val

    traverseBTree(root.right)


if __name__ == '__main__':

    A = [1,0,2]
    root = createBTree(A)
    traverseBTree(root)

    solution = Solution()
    # r_root = solution.trimBST(A, 1, 2)
    # traverseBTree(r_root)

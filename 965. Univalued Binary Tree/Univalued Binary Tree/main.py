# -*- coding: utf-8 -*-

# A binary tree is univalued if every node in the tree has the same value.
#
# Return true if and only if the given tree is univalued.

# Example 1:
#
#
# Input: [1,1,1,1,1,null,1]
# Output: true

# Example 2:
#
#
# Input: [2,2,2,5,2]
# Output: false

# Note:
#
# 1. The number of nodes in the given tree will be in the range [1, 100].
# 2. Each node's value will be an integer in the range [0, 99].


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.values = []

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if root is not None:
        #     self.isUnivalTree(root.left)
        #     self.isUnivalTree(root.right)
        #     self.values.append(root.val)
        #
        # return len(set(self.values)) == 1

        if root is None:
            return True

        if root.left is None and root.right is None:
            return True
        elif root.left is not None and root.right is None:
            if root.left.val != root.val:
                return False
            else:
                return self.isUnivalTree(root.left)
        elif root.right is not None and root.left is None:
            if root.right.val != root.val:
                return False
            else:
                return self.isUnivalTree(root.right)
        else:
            if root.right.val != root.val or root.left.val != root.val:
                return False
            else:
                return self.isUnivalTree(root.right) and\
                       self.isUnivalTree(root.left)

if __name__ == '__main__':
    node1 = TreeNode(1)
    node1.left = None
    node1.right = None

    node2 = TreeNode(1)
    node2.left = None
    node2.right = None

    node3 = TreeNode(1)
    node3.left = node1
    node3.right = node2

    node4 = TreeNode(1)
    node4.left = None
    node4.right = None

    node5 = TreeNode(1)
    node5.left = None
    node5.right = node4

    node6 = TreeNode(1)
    node6.left = node3
    node6.right = node5

    solution = Solution()
    isUnivalued = solution.isUnivalTree(node6)

    print 'isUnivalued --- %d' % isUnivalued

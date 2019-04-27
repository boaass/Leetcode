# -*- coding:utf-8 -*-

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
# of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        N = len(nums)
        if N == 0:
            return

        root = TreeNode(nums[N/2])
        root.left = self.sortedArrayToBST(nums[:N/2])
        root.right = self.sortedArrayToBST(nums[N/2+1:])

        return root


def TraverseBTree(node):
    """
    :type node: TreeNode
    """

    if not node:
        return

    TraverseBTree(node.left)
    print node.val
    TraverseBTree(node.right)


if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    solution = Solution()
    r = solution.sortedArrayToBST(nums)
    TraverseBTree(r)
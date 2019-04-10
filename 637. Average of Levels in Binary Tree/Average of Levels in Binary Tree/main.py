# -*- coding:utf-8 -*-

# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# 1. The range of node's value is in the range of 32-bit signed integer.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        if not root:
            return []

        queue = [root]
        r_list = []

        while len(queue) > 0:
            avg = 0.0
            length = len(queue)
            for index in range(length):
                node = queue.pop(0)
                avg += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            r_list.append(avg/length)

        return r_list


def createBTree(A):
    """
    :type A: List<int>
    :return: TreeNode
    """

    root = TreeNode(A[0])
    queue = [root]

    index = 0

    while len(queue) > 0 and index < len(A) - 2:
        cur_node = queue.pop(0)

        index += 1
        if A[index]:
            cur_node.left = TreeNode(A[index])
            queue.append(cur_node.left)

        index += 1
        if A[index]:
            cur_node.right = TreeNode(A[index])
            queue.append(cur_node.right)

    return root


if __name__ == '__main__':
    A = [3, 9, 20, None, None, 15, 7]
    root = createBTree(A)
    solution = Solution()
    r_list = solution.averageOfLevels(root)
    print r_list
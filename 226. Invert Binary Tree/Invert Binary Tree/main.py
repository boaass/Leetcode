# -*- coding:utf-8 -*-

# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        # queue = [root]
        # while len(queue) > 0:
        #     cur_node = queue.pop(0)
        #     if cur_node.left:
        #         queue.append(cur_node.left)
        #     if cur_node.right:
        #         queue.append(cur_node.right)
        #
        #     cur_node.left, cur_node.right = cur_node.right, cur_node.left

        left_node = self.invertTree(root.left)
        right_node = self.invertTree(root.right)
        root.left = right_node
        root.right = left_node

        return root


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


def traverseBTree(root):
    """
    :type root: TreeNode
    """
    if not root:
        return

    print root.val
    traverseBTree(root.left)
    traverseBTree(root.right)


if __name__ == '__main__':
    A = [4, 2, 7, 1, 3, 6, 9]
    root = createBTree(A)
    solution = Solution()

    traverseBTree(root)

    print '-------'

    node = solution.invertTree(root)

    traverseBTree(node)

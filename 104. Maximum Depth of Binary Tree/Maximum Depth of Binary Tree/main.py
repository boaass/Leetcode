# -*- coding:utf-8 -*-

# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # queue = [root]
        #
        # depth = 0
        # while len(queue) > 0:
        #     depth += 1
        #
        #     for index in range(len(queue)):
        #         cur_root = queue.pop(0)
        #         if cur_root.left:
        #             queue.append(cur_root.left)
        #         if cur_root.right:
        #             queue.append(cur_root.right)
        #
        # return depth


def createBTree(A):
    """
    :type A: List<TreeNode>
    :return: TreeNode
    """
    root = TreeNode(A[0])
    queue = [root]

    index = 0
    while len(queue) > 0 and index < len(A) - 2:

        cur_node = queue.pop(0)

        index += 1
        if A[index] is not None:
            cur_node.left = TreeNode(A[index])
            queue.append(cur_node.left)

        index += 1
        if A[index] is not None:
            cur_node.right = TreeNode(A[index])
            queue.append(cur_node.right)

    return root


def traverseBTree(root):
    """
    :type root: TreeNode
    """

    queue = [root]
    while len(queue) > 0:
        root = queue.pop(0)

        print root.val
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)


if __name__ == '__main__':

    A = [3,9,20,None,None,15,7]
    root = createBTree(A)
    # traverseBTree(root)

    solution = Solution()
    depth = solution.maxDepth(root)

    print 'depth --- %d' % depth
# -*- coding:utf-8 -*-

# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their
# sum is equal to the given target.
#
# Example 1:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True

# Example 2:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        A = []
        queue = []
        while queue or root:
            while root:
                queue.append(root)
                root = root.left
            root = queue.pop()
            A.append(root.val)
            root = root.right

        for v in A:
            if k-v != v and k-v in A:
                return True

        return False


def createBTree(A):
    """
    :type A: List[int] 
    :return: TreeNode
    """
    root = TreeNode(A[0])
    queue = [root]
    i = 0
    while len(queue) > 0 and i < len(A):
        cur_node = queue.pop(0)
        i += 1
        if i < len(A) and A[i] != None:
            cur_node.left = TreeNode(A[i])
            queue.append(cur_node.left)
        i += 1
        if i < len(A) and A[i] != None:
            cur_node.right = TreeNode(A[i])
            queue.append(cur_node.right)

    return root


def traverseBTree(root):
    """
    :type root: TreeNode 
    """
    if not root:
        return

    # 前序遍历
    # queue = []
    # while len(queue) > 0 or root:
    #     while root:
    #         print root.val
    #         queue.append(root)
    #         root = root.left
    #     root = queue.pop()
    #     root = root.right

    # 中序遍历
    # queue = []
    # while len(queue) > 0 or root:
    #     while root:
    #         queue.append(root)
    #         root = root.left
    #     root = queue.pop()
    #     cur_root = root
    #     print root.val
    #     root = root.right

    # 后续遍历
    # stack1 = []
    # stack2 = []
    # while len(stack1) > 0 or root:
    #     while root:
    #         stack1.append(root)
    #         stack2.append(root)
    #         root = root.right
    #     root = stack1.pop()
    #     root = root.left
    #
    # while len(stack2) > 0:
    #     root = stack2.pop()
    #     print root.val


if __name__ == '__main__':
    A = [5, 3, 6, 2, 4, None, 7]
    root = createBTree(A)
    traverseBTree(root)

    # solution = Solution()
    # r = solution.findTarget(root, 9)
    # print r
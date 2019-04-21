# -*- coding:utf-8 -*-

# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed
# to the original key plus sum of all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        stack1 = []
        sum_val = 0
        cur_node = root
        while len(stack1) > 0 or root:
            while root:
                stack1.append(root)
                root = root.right
            root = stack1.pop()
            if root.val != None:
                temp = root.val
                root.val += sum_val
                sum_val += temp
            root = root.left

        return cur_node


def createBTree(A):
    """
    :type A: List[int] 
    :return: TreeNode
    """
    root = TreeNode(A[0])
    queue = [root]
    i = 0
    while len(queue) > 0:
        cur_node = queue.pop(0)
        i += 1
        if i < len(A) and A[i]:
            cur_node.left = TreeNode(A[i])
            queue.append(cur_node.left)

        i += 1
        if i < len(A) and A[i]:
            cur_node.right = TreeNode(A[i])
            queue.append(cur_node.right)

    return root


def traverseBTree(root):
    """
    :type root: TreeNode 
    """
    if not root:
        return

    stack1 = []
    stack2 = []

    while len(stack1) > 0 or root:
        while root:
            stack1.append(root)
            root = root.right
        root = stack1.pop()
        # print root.val
        stack2.append(root)
        root = root.left

    while len(stack2) > 0:
        root = stack2.pop(0)
        print root.val


if __name__ == '__main__':
    A = [2,0,3,-4,1]
    root = createBTree(A)
    # traverseBTree(root)

    solution = Solution()
    r_node = solution.convertBST(root)
    traverseBTree(r_node)
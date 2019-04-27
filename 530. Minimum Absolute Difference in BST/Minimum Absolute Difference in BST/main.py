# coding:utf-8 -*-

# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two
#  nodes.
#
# Example:
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

# Note: There are at least two nodes in this BST.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack1 = []
        stack2 = []
        node = root
        while stack1 or node:
            while node:
                stack1.append(node)
                node = node.left
            node = stack1.pop()
            stack2.append(node)
            node = node.right

        return min(abs(stack2[i+1].val - stack2[i].val) for i in range(0, len(stack2)-1))


def createBTree(nodeList):
    """
    :type nodeList: List[int] 
    :return: TreeNode
    """
    root = TreeNode(A[0])
    temp_queue = [root]
    i = 0
    while i < len(A):
        queue = temp_queue
        temp_queue = []
        # print i
        while len(queue) > 0:
            cur_node = queue.pop(0)
            # print cur_node.val
            if cur_node == None:
                i += 2
                continue
            i += 1
            if i < len(A) and A[i] != None:
                cur_node.left = TreeNode(A[i])
                temp_queue.append(cur_node.left)
            elif i >= len(A):
                continue
            elif A[i] == None:
                temp_queue.append(None)
            i += 1
            if i < len(A) and A[i] != None:
                cur_node.right = TreeNode(A[i])
                temp_queue.append(cur_node.right)
            elif i >= len(A):
                continue
            elif A[i] == None:
                temp_queue.append(None)

    return root


def travelBTree(root):
    """
    :type root: TreeNode 
    """
    if not root:
        return

    travelBTree(root.left)
    print root.val
    travelBTree(root.right)


if __name__ == '__main__':
    A = [1, None, 3, None, None, 2]
    root = createBTree(A)
    # travelBTree(root)
    solution = Solution()
    r = solution.getMinimumDifference(root)
    print r
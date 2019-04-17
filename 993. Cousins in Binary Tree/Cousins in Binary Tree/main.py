# -*- coding:utf-8 -*-

# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
#
# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
#
# Note:
#
# 1. The number of nodes in the tree will be between 2 and 100.
# 2. Each node has a unique integer value from 1 to 100.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        queue = [root]
        while len(queue) > 0:
            v_d = {}
            for i in range(len(queue)):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                    v_d[cur_node.left.val] = cur_node.val
                if cur_node.right:
                    queue.append(cur_node.right)
                    v_d[cur_node.right.val] = cur_node.val

            if x in v_d.keys() and y in v_d.keys() and v_d[x] != v_d[y]:
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
        if i >= len(A):
            break
        cur_node.left = TreeNode(A[i])
        queue.append(cur_node.left)

        i += 1
        if i >= len(A):
            break
        cur_node.right = TreeNode(A[i])
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
    A = [1, 2, 3, None, 4]
    root = createBTree(A)
    # traverseBTree(root)

    x = 2
    y = 3
    solution = Solution()
    r = solution.isCousins(root, x, y)

    print r
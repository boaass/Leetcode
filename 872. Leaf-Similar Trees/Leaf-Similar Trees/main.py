# -*- coding:utf-8 -*-

# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value
# sequence.

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Note:
#
# Both of the given trees will have between 1 and 100 nodes.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def traverseNode(node, queue):
            if node is None:
                return None

            l_node = traverseNode(node.left, queue)
            r_node = traverseNode(node.right, queue)
            if l_node is None and r_node is None:
                queue.append(node.val)

            return node

        if root1 is None or root2 is None:
            return False

        nodeQueue1 = []
        nodeQueue2 = []

        traverseNode(root1, nodeQueue1)
        traverseNode(root2, nodeQueue2)

        if cmp(nodeQueue1, nodeQueue2) == 0:
            return True
        else:
            return False




if __name__ == '__main__':

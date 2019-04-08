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

            print node.val

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


def traversalBinaryTree(root):
    """
    :type root: TreeNode
    """
    if root is None:
        return

    print root.val
    traversalBinaryTree(root.left)
    traversalBinaryTree(root.right)


def breadthTraversalCreateBinaryTree(A):
    """
    :type A: List<Int>
    :rtype: TreeNode
    """
    index = 0
    root = TreeNode(A[index])
    queue = [root]
    while len(queue) > 0 and index < len(A)-2:
        lastNode = queue.pop(0)
        index += 1
        if A[index] is not None:
            lastNode.left = TreeNode(A[index])
            queue.append(lastNode.left)
        index += 1
        if A[index] is not None:
            lastNode.right = TreeNode(A[index])
            queue.append(lastNode.right)
    return root


if __name__ == '__main__':
    node1 = breadthTraversalCreateBinaryTree([3,5,1,6,2,9,8,None,None,7,4])
    node2 = breadthTraversalCreateBinaryTree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])

    solution = Solution()
    isLeafSimilar = solution.leafSimilar(node1, node2)
    print 'isLeafSimilar --- %d' % isLeafSimilar
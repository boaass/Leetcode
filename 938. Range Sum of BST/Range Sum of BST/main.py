# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (
# inclusive).
#
# The binary search tree is guaranteed to have unique values.
#
# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
#
# Note:
#
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeManager(object):
    def CreateBinaryTree(self, vals):
        root = TreeNode(vals[0])
        last_nodes = [root]
        for i in range(1, len(vals)):
            if i % 2 == 1:
                # left
                if vals[i]:
                    node = last_nodes[0]
                    node.left = TreeNode(vals[i])
                    last_nodes.append(node.left)
            else:
                node = last_nodes.pop(0)
                if vals[i]:
                    node.right = TreeNode(vals[i])
                    last_nodes.append(node.right)

        return root

    def TraverseBinaryTree(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            print node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        # return self.inOrderSum(root, L, R)
        return self.preOrderSum(root, L, R)

    def preOrderSum(self, root, L, R):
        r = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                r += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return r


    def inOrderSum(self, root, L, R):
        if not root:
            return 0
        r = 0
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if R >= node.val >= L:
                    r += node.val
                node = node.right

        return r


if __name__ == '__main__':
    vals = [10, 5, 15, 3, 7, None, 18]
    L = 7
    R = 15

    b = BinaryTreeManager()
    root = b.CreateBinaryTree(vals)
    # b.TraverseBinaryTree(root)

    s = Solution()
    print s.rangeSumBST(root, L, R)
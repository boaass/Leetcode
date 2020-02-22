# coding=utf-8
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeManager(object):

    def createBinaryTree(self, vals):
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
                # right
                node = last_nodes.pop(0)
                if vals[i]:
                    node.right = TreeNode(vals[i])
                    last_nodes.append(node.right)

        return root

    def traversBinaryTree(self, root):
        # 层级遍历
        if not root:
            return

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                r.append(node.val)
                node = node.right

        return r


if __name__ == '__main__':
    b = BinaryTreeManager()
    vals = [1,None,2,3]
    root = b.createBinaryTree(vals)
    # b.traversBinaryTree(root)
    s = Solution()
    print s.inorderTraversal(root)
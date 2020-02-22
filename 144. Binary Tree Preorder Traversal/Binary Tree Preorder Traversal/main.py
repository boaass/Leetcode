# Given a binary tree, return the preorder traversal of its nodes' values.
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
# Output: [1,2,3]
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
        last_node = [root]
        for i in range(1, len(vals)):
            if i % 2 == 1:
                # left
                if vals[i]:
                    node = last_node[0]
                    node.left = TreeNode(vals[i])
                    last_node.append(node.left)
            else:
                # right
                node = last_node.pop(0)
                if vals[i]:
                    node.right = TreeNode(vals[i])
                    last_node.append(node.right)

        return root

    def traverersBinaryTree(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            print node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        r = []
        stack = [root]
        while stack:
            node = stack.pop()
            r.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return r


if __name__ == '__main__':
    vals = [1,None,2,3]
    b = BinaryTreeManager()
    root = b.createBinaryTree(vals)
    # b.traverersBinaryTree(root)

    s = Solution()
    print s.preorderTraversal(root)
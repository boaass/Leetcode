# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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

    def traverseBinaryTree(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            print node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        stack1 = [root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        r = []
        while stack2:
            r.append(stack2.pop())
        return r


if __name__ == '__main__':
    vals = [1,None,2,3]
    b = BinaryTreeManager()
    root = b.createBinaryTree(vals)
    # b.traverseBinaryTree(root)
    s = Solution()
    print s.postorderTraversal(root)
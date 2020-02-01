# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createNode(vals):
    """
    :param vals: List<Int>
    :return: TreeNode
    """
    head = node = TreeNode(vals.pop(0))
    nodes = [node]
    index = 0
    while 1:
        index += 1
        for i in range(pow(2, index-1)):
            node = nodes.pop(0)
            if len(vals) > 0:
                cur_val = vals.pop(0)
                if cur_val is not None:
                    node.left = TreeNode(cur_val)
                    nodes.append(node.left)

            if len(vals) > 0:
                cur_val = vals.pop(0)
                if cur_val is not None:
                    node.right = TreeNode(cur_val)
                    nodes.append(node.right)

        if len(vals) == 0:
            return head


def traverseNode(root):
    nodes = [root]
    while len(nodes) > 0:
        node = nodes.pop(0)
        print node.val
        if node.left is not None:
            nodes.append(node.left)
        if node.right is not None:
            nodes.append(node.right)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = [(root, root)]
        while len(stack) > 0:
            node_left, node_right = stack.pop()
            if node_left is None and node_right is None:
                pass
            elif node_left is None or node_right is None:
                return False
            elif node_left.val != node_right.val:
                return False
            else:
                stack.append((node_left.left, node_right.right))
                stack.append((node_left.right, node_right.left))

        return True




if __name__ == '__main__':
    root = createNode([1,2,2,None,3,None,3])
    # traverseNode(root)
    s = Solution()
    print s.isSymmetric(root)
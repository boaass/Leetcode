# *- coding:utf-8 -*-

# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack1 = []
        stack2 = []
        r_sum = 0

        while root or stack1:
            while root:
                stack1.append(root)
                root = root.left
                if root != None:
                    stack2.append(root.val)
            root = stack1.pop()
            root = root.right
            if not root:
                if stack2:
                    r_sum += stack2.pop()
            stack2 = []

        return r_sum


def createBTree(A):
    """
    :param A: List[int] 
    :return: TreeNode
    """
    root = TreeNode(A[0])
    queue = [root]
    i = 0

    while queue and i < len(A):
        cur_node = queue.pop(0)
        i += 1
        if i < len(A) and A[i] != None:
            cur_node.left = TreeNode(A[i])
            queue.append(cur_node.left)
        i += 1
        if i < len(A) and A[i] != None:
            cur_node.right = TreeNode(A[i])
            queue.append(cur_node.right)

    return root


def traverseBTree(root):
    """
    :param root: TreeNode 
    """
    if not root:
        return

    traverseBTree(root.left)
    print root.val
    traverseBTree(root.right)


if __name__ == '__main__':
    A = [0,2,4,1,None,3,-1,5,1,None,6,None,8]
    root = createBTree(A)
    # traverseBTree(root)

    solution = Solution()
    r = solution.sumOfLeftLeaves(root)
    print r

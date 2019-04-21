# -*- coding:utf-8 -*-

# You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing
#  way.
#
# The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty
# parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary
# tree.
#
# Example 1:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
#
# Output: "1(2(4))(3)"
#
# Explanation: Originallay it needs to be "1(2(4)())(3()())",
# but you need to omit all the unnecessary empty parenthesis pairs.
# And it will be "1(2(4))(3)".
# Example 2:
# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4
#
# Output: "1(2()(4))(3)"
#
# Explanation: Almost the same as the first example, except we can't omit the first parenthesis pair to break the
# one-to-one mapping relationship between the input and the output.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""

        left = (self.tree2str(t.left) if t.left else None)
        right = (self.tree2str(t.right) if t.right else None)
        out = str(t.val)
        if left and right:
            out = out + "(" + left + ')' + "(" + right + ")"
        elif right:
            out = out + "()" + "(" + right + ")"
        elif left:
            out = out + "(" + left + ")"

        return out


def createBTree(A):
    """
    :type A: List[int] 
    :return: TreeNode
    """
    root = TreeNode(A[0])
    queue = [root]
    i = 0
    while len(queue) > 0:
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


if __name__ == '__main__':
    A = [1,2,3,4,None,5,6]
    t = createBTree(A)
    solution = Solution()
    r = solution.tree2str(t)
    print r
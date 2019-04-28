# coding:utf-8 -*-
#
# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def traverse_and_save(root):
            """
            :type root: TreeNode 
            :return: List[int]
            """
            if not root:
                return None

            r = [root.val]
            temp_queue = [root]
            while temp_queue:
                queue = temp_queue
                while queue:
                    cur_node = queue.pop(0)
                    if cur_node.left:
                        temp_queue.append(cur_node.left)
                        r.append(cur_node.left.val)
                    else:
                        r.append(0)
                    if cur_node.right:
                        temp_queue.append(cur_node.right)
                        r.append(cur_node.right.val)
                    else:
                        r.append(0)

            for i in range(len(r)-1, -1, -1):
                if r[i] == 0:
                    r.pop(-1)
                else:
                    break

            return r


        A = traverse_and_save(p)
        B = traverse_and_save(q)

        return A == B


def createBTree(A):
    """
    :type A: List[int]
    :return: TreeNode
    """
    root = TreeNode(A[0])
    queue = [root]
    i = 0
    while i < len(A):
        while queue:
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
    :type root: TreeNode 
    """
    if not root:
        return

    temp_queue = [root]
    while temp_queue:
        queue = temp_queue
        while queue:
            cur_node = queue.pop(0)
            print cur_node.val
            if cur_node.left:
                temp_queue.append(cur_node.left)
            if cur_node.right:
                temp_queue.append(cur_node.right)


if __name__ == '__main__':
    A = [1, 2, 1]
    B = [1, None, 2]
    p = createBTree(A)
    q = createBTree(B)

    # traverseBTree(p)
    # traverseBTree(q)

    solution = Solution()
    r = solution.isSameTree(p, q)
    print r
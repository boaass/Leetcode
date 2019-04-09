# -*- coding:utf-8 -*-

# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example, given a 3-ary tree:

# We should return its level order traversal:
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]

# Note:
#
# 1. The depth of the tree is at most 1000.
# 2. The total number of nodes is at most 5000.


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return None

        r_list = []
        queue = [root]

        while len(queue) > 0:
            t_n_queue = []
            t_v_queue = []
            for node in queue:
                t_v_queue.append(node.val)
                if node.children:
                    t_n_queue += node.children
            queue = t_n_queue
            r_list.append(t_v_queue)

        return r_list


def createThirdTree(A):
    """
    :type A: List<List<Int>>
    :return: Node
    """
    root = Node(A[0], None)

    queue = [root]

    index = 0
    while len(queue) > 0 and index < len(A) - 3:
        cur_node = queue.pop(0)
        children = []
        for i in range(3):
            index += 1
            if A[index]:
                children.append(Node(A[index], None))
            # print A[index]
        cur_node.children = children
        queue += children

    return root


if __name__ == '__main__':
    A = [1, 3, 2, 4, 5, 6, None]
    root = createThirdTree(A)

    solution = Solution()
    v_list = solution.levelOrder(root)

    print v_list
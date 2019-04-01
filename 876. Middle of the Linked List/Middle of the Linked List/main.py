# -*- coding: utf-8 -*-

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#
# If there are two middle nodes, return the second middle node.

# Example 1:
#
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:
#
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.

# Note:
#
# The number of nodes in the given list will be between 1 and 100.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # if head is None:
        #     return None
        #
        # first_p = second_p = head
        #
        # while first_p is not None and second_p is not None and second_p.next is not None:
        #
        #     print "%d, %d" % (first_p.val, second_p.val)
        #
        #     first_p = first_p.next
        #     second_p = second_p.next.next
        #
        # return first_p

        if head is None:
            return None

        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A)/2]



if __name__ == '__main__':
    node6 = ListNode(6)
    node6.next = None
    node5 = ListNode(5)
    node5.next = node6
    node4 = ListNode(4)
    node4.next = node5
    node3 = ListNode(3)
    node3.next = node4
    node2 = ListNode(2)
    node2.next = node3
    node1 = ListNode(1)
    node1.next = node2

    solution = Solution()
    r_node = solution.middleNode(node1)
    print 'result value --- %d' % r_node.val


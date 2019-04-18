# -*- codin:utf-8 -*-

# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # new_head = None
        # while head:
        #     p = head
        #     head = head.next
        #     p.next = new_head
        #     new_head = p
        #
        # return new_head

        if not head or not head.next:
            return head

        p = head.next
        new_head = self.reverseList(p)

        head.next = None
        p.next = head
        return new_head


def createList(A):
    """
    :type A: List[int] 
    :return: ListNode
    """
    head = ListNode(A[0])
    cur_node = head
    for i in range(1, len(A)):
        cur_node.next = ListNode(A[i])
        cur_node = cur_node.next

    return head


def traverseList(head):
    """
    :type head: ListNode 
    """

    cur_node = head
    while cur_node:
        print cur_node.val
        cur_node = cur_node.next


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    head = createList(A)

    solution = Solution()
    node = solution.reverseList(head)

    traverseList(node)
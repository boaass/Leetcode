# -*- coding:utf-8 -*-


# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the
# nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None and l2 is None:
            return None

        l1_cur_node = l1
        l2_cur_node = l2

        head = r_l = ListNode(0)
        while l1_cur_node is not None and l2_cur_node is not None:
            new_node = ListNode(0)

            if l1_cur_node.val <= l2_cur_node.val:
                new_node.val = l1_cur_node.val
                l1_cur_node = l1_cur_node.next
            else:
                new_node.val = l2_cur_node.val
                l2_cur_node = l2_cur_node.next

            r_l.next = new_node
            r_l = r_l.next

        while l1_cur_node is not None or l2_cur_node is not None:
            new_node = ListNode(0)
            if l1_cur_node is None:
                new_node.val = l2_cur_node.val
                l2_cur_node = l2_cur_node.next
            elif l2_cur_node is None:
                new_node.val = l1_cur_node.val
                l1_cur_node = l1_cur_node.next
            r_l.next = new_node
            r_l = r_l.next

        return head.next


    def printListNode(self, l):
        """
        :param l: ListNode
        """
        if l is None:
            return

        print l.val
        self.printListNode(l.next)


if __name__ == '__main__':
    l12 = ListNode(4)
    l11 = ListNode(2)
    l11.next = l12
    l1 = ListNode(1)
    l1.next = l11

    l22 = ListNode(4)
    l21 = ListNode(3)
    l21.next = l22
    l2 = ListNode(1)
    l2.next = l21

    s = Solution()
    r = s.mergeTwoLists(l1, l2)
    s.printListNode(r)
# coding=utf-8
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        last = slow.next
        pre = head

        # 翻转后半部分链表
        while last.next:
            temp = last.next
            last.next = temp.next
            temp.next = slow.next
            slow.next = temp

        # newHead = None
        # while last:
        #     node = last
        #     last = last.next
        #
        #     node.next = newHead
        #     newHead = node
        #
        # slow.next = newHead

        while slow.next:
            slow = slow.next
            print pre.val, slow.val
            if pre.val != slow.val:
                return False
            pre = pre.next

        return True

    def reversedLinkedList(self, head):
        newHead = None
        while head:
            node = head
            head = head.next
            node.next = newHead
            newHead = node

        return newHead

    def createLinkList(self, vals, pos):
        before_node = None
        last_node = None
        for i in range(len(vals) - 1, -1, -1):
            node = ListNode(vals[i])
            node.next = before_node
            before_node = node

            if i == len(vals) - 1:
                last_node = node
            if pos != -1 and pos == i:
                last_node.next = node
        return before_node

    def traverseLinkedList(self, head):
        while head:
            print head.val
            head = head.next

if __name__ == '__main__':

    s = Solution()
    head = s.createLinkList([1, 2, 3, 3, 2, 1], -1)
    print s.isPalindrome(head)
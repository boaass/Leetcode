# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeManager(object):
    def createNodeList(self, vals):
        """
        :param vals: List
        :return: ListNode
        """

        last_node = ListNode(vals[0])
        head = last_node
        for v in vals[1:]:
            node = ListNode(v)
            last_node.next = node
            last_node = node

        return head

    def traverseNodeList(self, head):
        while head:
            print head.val
            head = head.next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """2
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # two pass
        # return self.twoPassMethod(head, n)

        # one pass
        return self.onePassMethod(head, n)

    def onePassMethod(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head

    def twoPassMethod(self, head, n):
        cur_node = head
        count = 0
        while cur_node:
            cur_node = cur_node.next
            count += 1

        if count < n:
            return head
        if count == n:
            head = head.next
            return head

        cur_node = head
        index = 1
        while cur_node:
            if index == count - n:
                cur_node.next = cur_node.next.next
                break
            cur_node = cur_node.next
            index += 1

        return head

if __name__ == '__main__':
    vals = [1, 2, 3, 4, 5]
    manager = ListNodeManager()
    head = manager.createNodeList(vals)
    # manager.traverseNodeList(head)
    s = Solution()
    r = s.removeNthFromEnd(head, 2)
    manager.traverseNodeList(r)

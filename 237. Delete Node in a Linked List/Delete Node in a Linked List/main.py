# -*- coding:utf-8 -*-

# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Given linked list -- head = [4,5,1,9], which looks like following:

# Example 1:
#
# Input: head = [4,5,1,9], node = 5 Output: [4,1,9] Explanation: You are given the second node with value 5,
# the linked list should become 4 -> 1 -> 9 after calling your function. Example 2:
#
# Input: head = [4,5,1,9], node = 1 Output: [4,5,9] Explanation: You are given the third node with value 1,
# the linked list should become 4 -> 5 -> 9 after calling your function.

# Note:
#
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self, head):
        """
        :type head: ListNode
        """
        self.head = head

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

        # head = last_node = self.head
        # while head:
        #     if head.val == node.val:
        #         next_node = head.next
        #         last_node.next = next_node
        #         return
        #     last_node = head
        #     head = head.next


def createList(A):
    """
    :type A: List[int]
    :return: ListNode
    """
    head = ListNode(A[0])
    last_node = head
    for i in range(1, len(A)):
        cur_node = ListNode(A[i])
        last_node.next = cur_node
        last_node = cur_node

    return head


def traverseList(head):
    """
    :type head: ListNode
    """
    while head:
        print head.val
        head = head.next


if __name__ == '__main__':
    A = [4, 5, 1, 9]
    head = createList(A)
    # traverseList(head)

    del_node = None
    cur_node = head
    while cur_node:
        if cur_node.val == 5:
            del_node = cur_node
            break
        cur_node = cur_node.next

    solution = Solution(head)
    solution.deleteNode(del_node)

    traverseList(solution.head)

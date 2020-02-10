# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
# the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # O(1) memery
        # return self.hasCycleWithO1Memery(head)

        # hash
        return self.hasCycleWithHash(head)

    def hasCycleWithO1Memery(self, head):
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

    def hasCycleWithHash(self, head):
        if head is None:
            return False
        nodesDict = {}
        node = head
        while node:
            if node not in nodesDict.keys():
                nodesDict[node] = 1
                node = node.next
            else:
                return True
        return False

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

    def traverseLinkList(self, head, pos):
        node = head
        node_list = []
        while node:
            if pos != -1 and len(node_list) > pos and node == node_list[pos]:
                return
            print node.val
            node_list.append(node)
            node = node.next


if __name__ == '__main__':
    vals = [3,2,0,-4]
    pos = 1
    s = Solution()
    head = s.createLinkList(vals, pos)
    # s.traverseLinkList(head, pos)
    print s.hasCycle(head)

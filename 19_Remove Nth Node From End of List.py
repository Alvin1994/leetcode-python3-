# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return ListNode(0)
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast and n + 1 > 0:
            fast = fast.next
            n -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next
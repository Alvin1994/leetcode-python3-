# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        assert isinstance(x, int)
        
        if not head:
            return
        
        b_head = ListNode(0)
        a_head = ListNode(0)
        a, b = a_head, b_head
        
        while head:
            if head.val < x:
                b.next = head
                b = b.next
            else:
                a.next = head
                a = a.next
            head = head.next
        b.next = a_head.next
        a.next = None
        return b_head.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return 
        
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next and node.next.next:
            a, b = node.next, node.next.next
            node.next = b
            a.next = b.next
            b.next = a
            node = node.next.next
            
        return dummy.next
            
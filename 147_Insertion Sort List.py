# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        
        dummy = ListNode(0)
        dummy.next = head
        n = head.next
        prev_n = head
        while n:
            i = dummy.next
            prev_i = dummy
            while i != n and n.val > i.val:
                i = i.next
                prev_i = prev_i.next
            if i == n:
                n = n.next
                prev_n = prev_n.next
                continue
            prev_n.next = n.next
            prev_i.next = n
            n.next = i
            n = prev_n.next
        return dummy.next
                
            
        
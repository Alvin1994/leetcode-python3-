# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        assert isinstance(m, int) and isinstance(n, int) and n>=m
        
        if not head:
            return 
        
        prev, curt = None, head
        
        while m > 1:
            prev = curt
            curt = curt.next
            m -= 1
            n -= 1
        left = prev
        tail = curt
        while n >= 1:
            tmp = curt.next
            curt.next = prev
            prev = curt
            curt = tmp
            n -= 1
        if left:
            left.next = prev
        else:
            head = prev
        tail.next = curt
        return head
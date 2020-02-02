# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        n = head
        stack = []
        while n:
            stack.append(n)
            n = n.next
        
        while stack:
            n = stack.pop(0)
            if stack:
                n.next = stack.pop()
            else:
                n.next = None
                break
            n = n.next
            if stack:
                n.next = stack[0]
            else:
                n.next = None
        return head
                
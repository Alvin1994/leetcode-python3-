# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        memo = head
        rst = head
        while head and head.next:
            if head.val != head.next.val:
                memo = memo.next
                head = head.next
            else:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                memo.next= head
                memo = memo.next
        return rst
        
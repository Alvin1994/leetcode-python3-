# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        if head.next == None:
            return head
        def find_mid(head):
            if not head:
                return None
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                
            right_head = slow.next
            slow.next = None
            return right_head
        
        def merge(a,b):
            
            dummy = ListNode(0)
            curt = dummy
            while a and b:
                if a.val < b.val:
                    curt.next = a
                    a = a.next
                else:
                    curt.next = b
                    b = b.next
                curt = curt.next
            if a == None:
                curt.next = b
            if b == None:
                curt.next = a
            return dummy.next
        mid = find_mid(head)
        l = self.sortList(head)
        r = self.sortList(mid)
        return merge(l,r)
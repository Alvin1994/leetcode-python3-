# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return 
        i = head
        while i != slow:
            i = i.next
            slow = slow.next
        return i
        
#         # find the first meet point
#         slowPtr = head
#         fastPtr = head
#         zPtr = None
#         while slowPtr and fastPtr:
#             slowPtr = slowPtr.next
#             if fastPtr.next is None or fastPtr.next.next is None:
#                 return None
#             else:
#                 fastPtr = fastPtr.next.next
#             if slowPtr == fastPtr:
#                 zPtr = slowPtr
#                 break
            
#         # find K by the condition 
#         # K+Z = -(2n-m)Y, m>n
#         kPtr = head
#         while kPtr:
#             if kPtr == zPtr:
#                 return kPtr
#             kPtr = kPtr.next
#             zPtr = zPtr.next
#         return None
            
            
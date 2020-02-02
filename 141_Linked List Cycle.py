# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast = head, head 
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
    def findCycleCross(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast, k = head, head, None
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                k = slow
                break
        if k: 
            i = head
            while i != k:
                i, k = i.next, k.next
            print(i.val)
            return i
        else:
            return False
        
                
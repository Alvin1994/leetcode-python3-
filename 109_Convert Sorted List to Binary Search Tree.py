# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        def find_mid(head):
            if not head:
                None
            s = head
            f = head
            prev = None
            while f and f.next:
                prev = s
                s = s.next
                f = f.next.next
            if prev:
                prev.next = None
            return s
        
        mid = find_mid(head)
        n = TreeNode(mid.val)
        if mid==head:
            return n
        n.left = self.sortedListToBST(head)
        n.right = self.sortedListToBST(mid.next)
        return n 
#     def sortedListToBST(self, head):
#         """
#         :type head: ListNode
#         :rtype: TreeNode
#         """
#         # 1. CovertListToArray : Time complexsity O(1)+O(log(N)) Space complexsity O(N)
#         # 2. Time complexsity O(N/2)*O(log(N)) Space complexsity O(log(N))
#         # using case 2
#         if not head:
#             return None
#         mid = self.findMiddle(head)
#         node = TreeNode(mid.val)
#         if head == mid:
#             return node
#         node.left = self.sortedListToBST(head)
#         node.right = self.sortedListToBST(mid.next)
#         return node
#     def findMiddle(self,head):
#         slowPt, fastPt, previousPt = head,head,None
#         while fastPt and fastPt.next:
#             previousPt = slowPt
#             slowPt = slowPt.next
#             fastPt = fastPt.next.next
#         if previousPt:
#             previousPt.next = None
#         return slowPt
    
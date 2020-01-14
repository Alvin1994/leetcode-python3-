class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        head = node
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                node, l1 = node.next, l1.next
            else:
                node.next = l2
                node, l2 = node.next, l2.next
            node.next = None
        if l1 or l2:
            if l1:
                a = l1
            else:
                a = l2
            while a:
                node.next = a 
                node, a = node.next, a.next
                node.next = None
        return head.next
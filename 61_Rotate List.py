# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        assert isinstance(k, int)
        
        if not head:
            return 
        if k == 0 or not head.next:
            return head
        
        break_node, end_node = head, head
        total_len = 1
        while k > 0 and end_node.next:
            end_node = end_node.next
            k -= 1
            total_len += 1
        if k != 0:
            k -= 1
            k %= total_len
            if k == 0:
                return head
            end_node = head
            while k > 0 and end_node.next:
                end_node = end_node.next
                k -= 1
            
        while end_node.next != None:
            break_node = break_node.next
            end_node = end_node.next
        new_head = break_node.next
        break_node.next = None
        end_node.next = head
        
        return new_head
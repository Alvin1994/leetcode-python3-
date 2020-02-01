"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        def helper(node):
            
            while node:
                head, tail = None, None
                while node:
                    if node.left:
                        if tail is None: # initial
                            head = node.left
                            tail = node.left
                        else:
                            tail.next = node.left
                            tail = tail.next
                    if node.right:
                        if tail is None: # initial
                            head = node.right
                            tail = node.right
                        else:
                            tail.next = node.right
                            tail = tail.next
                    node = node.next
                node = head
            return 
        helper(root)
        return root
    

                
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
            return 
        stack = [root]
        
        while stack:
            n = stack.pop()
            if n.left:
                stack.append(n.left)
                n.left.next = n.right
            if n.right:
                stack.append(n.right)
                if n.next:
                    n.right.next = n.next.left
        return root
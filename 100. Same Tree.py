# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        
        def helper(p,q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q) or p.val != q.val:
                return False
            return helper(p.left,q.left) and helper(p.right,q.right)
        return helper(p,q)
    
    def isSameTree_stack(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        
        if not p and not q:
            return True

        stack = [(p,q)]
        while stack:
            a,b = stack.pop()
            if not a and not b:
                continue
            if (a and not b) or (not a and b):
                return False
            if a.val != b.val:
                return False
            stack.append((a.left,b.left))
            stack.append((a.right,b.right))
        return True
            
    
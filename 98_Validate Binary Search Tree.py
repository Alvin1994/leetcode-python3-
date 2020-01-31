# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    
        def help_recursive(l,r,node):
            if not node:
                return True
            
            if l<node.val<r:
                return help_recursive(l,node.val, node.left) and help_recursive(node.val, r,node.right)
            return False
        
        return help_recursive(float('-inf'), float('inf'),root)
    def isValidBST2(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        stack = [(root,float('-inf'),float('inf'))]
        while stack:
            node,l,r = stack.pop()
            if node.val <= l or node.val >= r:
                return False
            if node.left:
                stack.append((node.left,l,node.val))
            if node.right:
                stack.append((node.right,node.val,r))
        return True
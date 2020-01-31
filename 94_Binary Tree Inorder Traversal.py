# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        # 1. RECURSIVE
        rst = []
        self.helper_recursive(root,rst)
        return rst
        
        # 2. STACK
        # return self.helper_stack(root)
    
    def helper_recursive(self, node, rst):
        if not node:
            return 
        self.helper_recursive(node.left, rst)
        rst.append(node.val)
        self.helper_recursive(node.right, rst)
        return 
    
    def helper_stack(self,node):
        stack = []
        rst = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack:
                break
            node = stack.pop()
            rst.append(node.val)
            node = node.right
        return rst
            
            
            
            
                
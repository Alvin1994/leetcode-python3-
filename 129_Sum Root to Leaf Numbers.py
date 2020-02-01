# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        self.rst = 0
        def helper(node,value):
            if not node:
                return 
            helper(node.left, value*10+node.val)
            helper(node.right, value*10+node.val)
            
            if not node.left and not node.right:
                self.rst += value*10 + node.val
                       
            return 
        helper(root, 0)
        return self.rst
        
        
    def sumNumbers2(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        stack = [(root, root.val)]
        rst = 0
        # DFS + stack
        while stack:
            node, val = stack.pop()
            if node.right is None and node.left is None:
                rst += val
            if node.right:
                stack.append((node.right, val*10 + node.right.val))
            if node.left:
                stack.append((node.left, val*10 + node.left.val))
        return rst
        
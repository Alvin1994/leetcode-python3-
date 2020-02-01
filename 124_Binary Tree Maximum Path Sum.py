# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        if not root:
            return False
        
        self.rst = float('-inf')
        self.helper(root)
        
        return self.rst
    def helper(self,node):
        if not node:
            return 0

        l_max = self.helper(node.left)
        r_max = self.helper(node.right)
        l_max = 0 if l_max < 0 else l_max
        r_max = 0 if r_max < 0 else r_max
        
        if l_max + r_max + node.val > self.rst:
            self.rst = l_max + r_max + node.val

        return node.val + max(l_max,r_max)
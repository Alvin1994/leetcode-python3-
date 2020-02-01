# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            if l == -1:
                return -1
            r = helper(node.right)
            if r == -1:
                return -1
            if abs(r-l) > 1:
                return -1
        
            return max(l,r) + 1
            
        return helper(root) != -1
        
#     # 1. bottom Down
#     def isBalanced(self, root: 'TreeNode') -> 'bool':
#         if not root:
#             return True
#         left = self.caculateDepth(root.left)
#         right = self.caculateDepth(root.right)
#         return abs(left-right)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
 
#     def caculateDepth(self, node:'TreeNode')-> 'int':
#         if node is None:
#             return 0
        
#         return max(self.caculateDepth(node.right),self.caculateDepth(node.left)) + 1
#     # 2. bottom Up
#     def isBalanced_bottomUp(self, root: 'TreeNode') -> 'bool':
#         return self.dfsHeight(root) != -1
#     def dfsHeight(self, node: 'TreeNode') -> 'int':
#         if node is None:
#             return 0
        
#         left = self.dfsHeight(node.left)
#         if left == -1:
#             return -1
#         right = self.dfsHeight(node.right)
#         if right ==-1:
#             return -1
        
#         if abs(left-right)>1:
#             return -1
#         return max(left,right)+1
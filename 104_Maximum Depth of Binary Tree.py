# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0
        return self._maxDepth(root,0)
    def _maxDepth(self, node,level):
        
        if node is None:
            return level
        return max(self._maxDepth(node.right,level+1), self._maxDepth(node.left,level+1))
        
        
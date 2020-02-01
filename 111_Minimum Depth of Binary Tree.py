# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        # caculate level by bottom Up
        # dfsHeight(node)->'int'
        def helper(node):
            childrens = [node.left,node.right]
            if not any(childrens):
                return 1
            minVal = float('inf')
            for children in childrens:
                if children:
                    minVal = min(minVal,helper(children))
            return minVal + 1
        
        if not root:
            return 0
        return helper(root)
    
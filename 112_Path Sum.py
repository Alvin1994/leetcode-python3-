# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        if not root:
            return False
        def helper(node,val):
            if not node:
                return False
            val -= node.val
            if node.left is None and node.right is None:
                return val == 0
            return helper(node.left, val) or helper(node.right, val)
        return helper(root,sum)

        
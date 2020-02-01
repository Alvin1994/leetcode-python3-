# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        memo = [root]
        prev = None
        while memo:
            n = memo.pop()
            if n.right:
                memo.append(n.right)
            if n.left:
                memo.append(n.left)
            if prev:
                prev.right = n
                prev.left = None
            prev = n
        return root
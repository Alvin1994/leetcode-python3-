# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        rst = []
        while stack:
            n = stack.pop()
            rst.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return rst
        
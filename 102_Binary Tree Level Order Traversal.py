# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        def helper(node, level,rst):
            if not node:
                return 
            if len(rst) < level + 1:
                rst.append([])
            rst[level].append(node.val)
            helper(node.left,level+1,rst)
            helper(node.right,level+1,rst)
            return 
        rst = []
        helper(root,0,rst)
        return rst
    def levelOrder2(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        stack = [(root,0)]
        rst = []
        while stack:
            n,level = stack.pop(0)
            if len(rst) < level + 1:
                rst.append([])
            rst[level].append(n.val)
            if n.left:
                stack.append((n.left, level+1))
            if n.right:
                stack.append((n.right, level+1))
        return rst
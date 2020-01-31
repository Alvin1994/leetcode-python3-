# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        
        if not root:
            return 
        stack = [(root,0)]
        rst = []
        
        while stack:
            n, level = stack.pop(0)
            if len(rst) < level + 1:
                rst.insert(0,[])
            rst[-(level+1)].append(n.val)
            if n.left:
                stack.append((n.left,level+1))
            if n.right:
                stack.append((n.right, level+1))
    
        return rst
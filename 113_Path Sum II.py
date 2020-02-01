# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        if not root:
            return []
        rst = []
        self.dfs(root,sum,[],rst)
        return rst

    def dfs(self,node,cost,path,rst):
        cost -= node.val
        if node.left:
            self.dfs(node.left,cost,path+[node.val],rst)
        if node.right:
            self.dfs(node.right,cost,path+[node.val],rst)
        
        if node.left is None and node.right is None and cost == 0:
            path.append(node.val)
            rst.append(path)
        return 
#     def pathSum2(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
#         if not root:
#             return []
#         rst = []
#         stack = [(root,sum,[])]
#         while stack:
#             node,cost,path = stack.pop()
#             if node.left:
#                 stack.append((node.left,cost-node.val,path+[node.val]))
#             if node.right:
#                 stack.append((node.right,cost-node.val,path+[node.val]))
#             if node.left is None and node.right is None and cost == node.val:
#                 path.append(node.val)
#                 rst.append(path)
#         return rst

        
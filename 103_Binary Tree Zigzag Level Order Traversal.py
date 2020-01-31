# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []
        rst = []
        return self._zigzagLevelOrder(root,0 ,rst)
    def _zigzagLevelOrder(self, node,level,rst):
        if node is None:
            return
        if len(rst) < level + 1:
            rst.append([])
        if level % 2 == 1:
            rst[level].insert(0,node.val)
        else:
            rst[level].append(node.val)
        self._zigzagLevelOrder(node.left,level+1,rst)
        self._zigzagLevelOrder(node.right,level+1,rst)
        
        return rst
            
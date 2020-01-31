# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        assert isinstance(n, int)
        if n<1:
            return 
        
        return self.helper(1,n)
    def helper(self, start, end):
        rst = []
        if start > end:
            return [None]
        
        for i in range(start, end+1, 1):
            l_list = self.helper(start, i-1)
            r_list = self.helper(i+1, end)
            for l_node in l_list:
                for r_node in r_list:
                    n = ListNode(i)
                    n.left = l_node
                    n.right = r_node
                    rst.append(n)
        return rst
        
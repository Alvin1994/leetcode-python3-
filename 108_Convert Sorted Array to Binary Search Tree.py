# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return 
        def helper(l,r):
            if l > r:
                return None
            mid = (l+r) // 2
            n = TreeNode(nums[mid])
            n.left = helper(l,mid-1)
            n.right = helper(mid+1,r)
            return n
        
        return helper(0,len(nums)-1)
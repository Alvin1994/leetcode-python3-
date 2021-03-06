class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        assert isinstance(nums, list)
        
        if not nums:
            return []
    
        def helper(l,r,tmp,rst):
            rst.append(tmp)
            if l > r:
                return
            for i in range(l,r+1,1):
                helper(i+1, r, tmp+[nums[i]], rst)
            return 
        rst = []
        helper(0, len(nums)-1, [], rst)
        return rst
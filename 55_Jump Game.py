class Solution:
    def canJump(self, nums: List[int]) -> bool:
        assert isinstance(nums, list)
        
        if not nums:
            return 
        tmp = nums[0]
        pos = 0
        for i, num in enumerate(nums):
            if tmp == 0:
                break
            tmp = max(tmp-1,num)
            pos = i
        return pos == len(nums)-1
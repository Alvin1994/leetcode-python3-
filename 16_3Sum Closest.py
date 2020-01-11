class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        assert isinstance(nums,list)
        
        if len(nums) < 3:
            return 
        nums.sort()
        rst = float('inf')
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1 
            r = len(nums) - 1
            while l < r:
                sum_ = nums[i] + nums[l]+ nums[r]
                if abs(target-sum_) < abs(target-rst):
                    rst = sum_
                if sum_ == target:
                    return rst
                elif sum_ < target:
                    l += 1
                else:
                    r -=1
        return rst
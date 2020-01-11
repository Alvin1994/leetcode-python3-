class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        assert isinstance(nums, list) and isinstance(target,int)
        
        nums_dict = Solution.initial_dict(nums)
        for i, num in enumerate(nums):
            value = target-num
            if value in nums_dict and nums_dict[value] != i:
                return [i, nums_dict[value]]
        return None
        
        
    def initial_dict(nums):
        rst = dict()
        for i, num in enumerate(nums):
            rst[num] = i
        return rst
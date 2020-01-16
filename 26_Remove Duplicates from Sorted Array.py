class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 
        index = 0
        for i in range(len(nums)):
            if i==0 or nums[i-1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index
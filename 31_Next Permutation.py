class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        assert isinstance(nums,list)
        if not nums:
            return 
        i = len(nums) - 2
        while i >= 0:
            j = len(nums) - 1
            index = None
            while j > i :
                s = nums[j] - nums[i]
                if s > 0 and (index==None or s < nums[index]-nums[i]):
                    index = j
                j -= 1
            if index != None:
                nums[index], nums[i] = nums[i], nums[index]
                break
            i -= 1 
        l,r = i + 1, len(nums)-1
        while r > l:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1
        return nums
            
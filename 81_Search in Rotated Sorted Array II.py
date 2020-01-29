class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        assert isinstance(nums, list) and isinstance(target, int)
        
        if not nums:
            return False
        l,r = 0, len(nums) -1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            while l < m and nums[l] == nums[m]:
                l += 1
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False
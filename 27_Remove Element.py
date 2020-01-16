class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        assert isinstance(nums, list) and isinstance(val, int)
        
        i, index = 0, len(nums) - 1
        while i <= index:
            if nums[i] == val:
                nums[i], nums[index] = nums[index], nums[i]
                index -= 1 
                continue
            i += 1 
        return index + 1
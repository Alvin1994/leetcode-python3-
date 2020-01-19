class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        assert isinstance(nums, list) and isinstance(target,int)
        if not nums:
            return [-1, -1]
        
        def binary_search(isEqual=True):
            l,r = 0, len(nums)-1
            if isEqual:
                while l<=r:
                    m = (l+r)//2
                    if target >= nums[m]:
                        l = m + 1
                    else:
                        r = m - 1
                if l-1 < 0 or target != nums[l-1]:
                    return -1
                else:
                    return l - 1
            else:
                while l<=r:
                    m = (l+r)//2
                    if target > nums[m]:
                        l = m + 1
                    else:
                        r = m - 1
                if r+1 == len(nums) or target != nums[r+1]:
                    return -1
                else:
                    return r + 1
        return [binary_search(False), binary_search(True)]
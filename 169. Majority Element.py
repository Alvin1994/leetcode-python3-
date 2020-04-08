class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    def majorityElement3(self, nums: List[int]) -> int:
        target = len(nums)//2 + 1
        count = dict()
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            if count[num] == target:
                return num
    def majorityElement2(self, nums: List[int]) -> int:
        
        target = (len(nums)-1)//2
        l, r = 0, len(nums)-1
        while l <= r:
            index = self.quickSort(nums, l, r)
            if index == target:
                return nums[index]
            if index < target:
                l = index + 1
            else:
                r = index - 1
        return -1
        
    def quickSort(self, nums, l, r):
        def selectPivot(nums, l, r):
            mid = (l+r)//2
            nums[mid], nums[r] = nums[r], nums[mid]
            return
        selectPivot(nums,l,r)
        i = l
        while l < r:
            if nums[l] <= nums[r]:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
            l += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i 
                
        
        
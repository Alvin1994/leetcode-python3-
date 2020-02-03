class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        mx = nums[0]
        mn = nums[0]
        rst = nums[0]
        
        for i in range(1,len(nums),1):
            if nums[i] > 0:
                mx = max(mx*nums[i], nums[i])
                mn = min(mn*nums[i], nums[i])
            else:
                tmp = mx
                mx = max(mn*nums[i], nums[i])
                mn = min(tmp*nums[i], nums[i])
            rst = max(mx,rst)
        return rst
    def maxProduct_badDP(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        mx = [0] * len(nums)
        mn = [0] * len(nums)
        
        mx[0] = nums[0]
        mn[0] = nums[0]
        rst = nums[0]
        
        for i in range(1,len(nums),1):
            mx[i] = max(max(mx[i-1]*nums[i], mn[i-1]*nums[i]),nums[i])
            mn[i] = min(min(mx[i-1]*nums[i], mn[i-1]*nums[i]),nums[i])
            rst = max(mx[i],rst)
        
            
        return rst
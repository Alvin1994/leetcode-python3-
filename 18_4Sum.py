class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        assert isinstance(nums,list), isinstance(target,int)
        
        def NSum(l,r,target,N,tmp_rst,rst): #pointer version
            if N < 2 or r-l+1 < N or target < nums[l]*N or target> nums[r]*N:# advantage of sort array: 
                return
            if N==2:
                while l < r:
                    if nums[l] + nums[r] == target:
                        rst.append(tmp_rst + [nums[l],nums[r]])
                        l += 1
                        while l<r and nums[l-1] == nums[l]:
                            l += 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l,r+1):
                    if i==l or (i > l and nums[i-1] != nums[i]):
                        NSum(i+1,r,target-nums[i],N-1,tmp_rst+[nums[i]],rst)
            return
        
        nums.sort()
        rst = []
        NSum(0,len(nums)-1,target,4,[],rst)
        return rst
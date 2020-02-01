lass Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        rst = 1
        memo = 1
        
        for i in range(1,len(nums),1):
            if nums[i] != nums[i-1]:
                if nums[i]-nums[i-1] == 1:
                    memo += 1
                else:
                    rst = max(rst,memo)
                    memo = 1
        return max(memo,rst)
                
        
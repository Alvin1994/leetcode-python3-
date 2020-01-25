class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tmp = 0
        rst = float('-inf')
        for value in nums:
            tmp = tmp + value
            if tmp > rst:
                rst = tmp
            if tmp <= 0:
                tmp = 0 
        return rst
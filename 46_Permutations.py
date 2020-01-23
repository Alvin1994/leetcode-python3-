class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        assert isinstance(nums,list)
        if not nums:
            return
        
        def dfs(path):
            if len(path) == len(nums):
                rst.append(path)
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    dfs(path + [nums[i]])
                    visited[i] = False
            return
        rst = []
        visited = [False] * len(nums)
        dfs([])
        return rst
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        assert isinstance(nums,list)
        if not nums:
            return
        def dfs(path):
            if len(path) == len(nums):
                rst.append(path)
            duplicates = dict()
            for i in range(len(nums)):
                if not visited[i]:
                    if nums[i] in duplicates:
                        continue
                    duplicates[nums[i]] = True
                    visited[i] = True
                    dfs(path + [nums[i]])
                    visited[i] = False
            return
        visited = [False] * len(nums)
        rst = []
        dfs([])
        return rst
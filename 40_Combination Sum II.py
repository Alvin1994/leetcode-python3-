class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        assert isinstance(candidates, list) and isinstance(target, int)
        
        if not candidates:
            return 
        def dfs(l,r,target,rst):
            if r+1<l or target < 0:
                return 
            if target == 0:
                return rsts.append(rst)
            for i in range(l,r+1,1):
                if candidates[i] > target:
                    break
                if i==l or candidates[i] != candidates[i-1]:
                    dfs(i+1,r,target-candidates[i],rst+[candidates[i]])
            return 
        rsts = []
        candidates.sort()
        dfs(0,len(candidates)-1,target,[])
        return rsts
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        assert isinstance(candidates, list) and isinstance(target, int)
        
        if not candidates:
            return 
        def findSum(l,r,curt_sum, rst):
            if l>r+1 or curt_sum > target:
                return
            if curt_sum == target:
                rsts.append(rst)
            for i in range(l,r+1,1):
                findSum(i, r, curt_sum+candidates[i], rst+[candidates[i]])
            return 
        rsts = []
        findSum(0,len(candidates)-1,0,[])
        return rsts
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        assert isinstance(n, int) and isinstance(k ,int)
        if n <= 0:
            return []

        def helper(l ,r, tmp,rst):
            if len(tmp) == k:
                rst.append(tmp)
                return 
            if l > r:
                return 
            
            for i in range(l, r+1, 1):
                helper(i+1, r, tmp+[nums[i]], rst)
            return
            
        nums = [x+1 for x in range(n)]
        rst = []
        helper(0, n-1,[],rst)
        return rst
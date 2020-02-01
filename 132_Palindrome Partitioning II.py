class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        memo = dict()
        def helper(l,r):
            if l > r:
                return 0
            minVal = float('inf')
            for i in range(l,r+1,1):
                strs = s[l:i+1]
                if strs == strs[::-1]:
                    if s[i+1:r+1] in memo:
                        minVal = min(memo[s[i+1:r+1]], minVal)
                    else:
                        minVal = min(helper(i+1,r), minVal)
            memo[s[l:r+1]] = minVal + 1 
            return memo[s[l:r+1]]
        helper(0,len(s)-1)
        
        return memo[s]-1 if memo[s] != float('inf') else 0
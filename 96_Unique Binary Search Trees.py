class Solution:
    def numTrees(self, n: int) -> int:
        assert isinstance(n, int)
        if n < 1:
            return 
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1,1):
            for j in range(0,i,1):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
            
    
    def numTrees2(self, n: int) -> int:    
        assert isinstance(n, int)
        
        if n < 1:
            return 
        def helper(start, end):
            if start > end:
                return 1
            count = 0
            for i in range(start,end+1,1):
                count += (helper(i+1, end) + helper(start,i-1))
            return count
        
        return self.helper(1,n)
    
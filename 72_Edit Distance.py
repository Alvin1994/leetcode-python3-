class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1)+1)]
        
        for c in range(len(dp[0])):
            dp[0][c] = c
        for r in range(len(dp)):
            dp[r][0] = r
        for r in range(1,len(dp),1):
            for c in range(1,len(dp[r]),1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(min(dp[r-1][c-1],dp[r-1][c]),dp[r][c-1]) + 1
        return dp[-1][-1]
        
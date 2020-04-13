class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        dp[-1][-1] = 1 if dungeon[-1][-1] >= 0 else 1 - dungeon[-1][-1]
        
        for r in range(len(dungeon)-2,-1,-1):
            dp[r][-1] = dp[r+1][-1] - dungeon[r][-1]
            dp[r][-1] = 1 if dp[r][-1] <= 0 else dp[r][-1]
        for c in range(len(dungeon[0])-2,-1,-1):
            dp[-1][c] = dp[-1][c+1] - dungeon[-1][c]
            dp[-1][c] = 1 if dp[-1][c] <= 0 else dp[-1][c]
            
        for c in range(len(dungeon[0])-2,-1,-1):
            for r in range(len(dungeon)-2,-1,-1):
                dp[r][c] = min(dp[r+1][c],dp[r][c+1]) - dungeon[r][c]
                dp[r][c] = 1 if dp[r][c] <= 0 else dp[r][c]
        return dp[0][0]
        
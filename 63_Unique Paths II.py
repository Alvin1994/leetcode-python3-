class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        assert isinstance(obstacleGrid, list)
        
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        for r in range(0, len(obstacleGrid), 1):
            for c in range(0, len(obstacleGrid[0]), 1):
                if obstacleGrid[r][c] == 0:
                    if r==0 and c==0:
                        continue
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]
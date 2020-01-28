class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list)
        
        if not grid or not grid[0]:
            return 0
        for r in range(1, len(grid), 1):
            grid[r][0] += grid[r-1][0]
        for c in range(1, len(grid[0]), 1):
            grid[0][c] += grid[0][c-1]
            
        for r in range(1, len(grid), 1):
            for c in range(1, len(grid[0]), 1):
                grid[r][c] += min(grid[r-1][c],grid[r][c-1])
        return grid[-1][-1]
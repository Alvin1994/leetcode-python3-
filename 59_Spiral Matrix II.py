class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        assert isinstance(n,int)
        
        if n <= 0:
            return []
        if n == 1:
            return [[1]]
        def get_i():
            self.i += 1
            return self.i
        self.i = 0
        rst = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        while bottom > top and right > left:
            for col in range(left, right+1, 1):
                rst[top][col] = get_i()
            top += 1
            for row in range(top,bottom+1,1):
                rst[row][right] = get_i()
            right -= 1
            for col in range(right,left-1,-1):
                rst[bottom][col] = get_i()
            bottom -= 1
            for row in range(bottom, top-1, -1):
                rst[row][left] = get_i()
            left += 1
        if bottom == top:
            for col in range(left, right+1, 1):
                rst[top][col] = get_i()
        elif right == left:
            for row in range(top,bottom+1,1):
                rst[row][left] = get_i()
        return rst
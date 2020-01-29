class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        assert isinstance(matrix, list)
        
        if not matrix:
            return 
        
        isRowZero, isColZero = False, False
        
        for r in range(0,len(matrix), 1):
            if matrix[r][0] == 0:
                isRowZero = True
                break
        for c in range(0,len(matrix[0]), 1):
            if matrix[0][c] == 0:
                isColZero = True
                break
        for r in range(1,len(matrix), 1):
            for c in range(1, len(matrix[0]), 1):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0, 0
        for r in range(1, len(matrix), 1):
            if matrix[r][0] == 0:
                for c in range(1, len(matrix[0]), 1):
                    matrix[r][c] = 0
            if isRowZero:
                matrix[r][0] = 0
        for c in range(1, len(matrix[0]), 1):
            if matrix[0][c] == 0:
                for r in range(1, len(matrix), 1):
                    matrix[r][c] = 0
            if isColZero:
                matrix[0][c] = 0
        if isRowZero or isColZero:
            matrix[0][0] = 0 
        return 
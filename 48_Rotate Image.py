class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        up,bottom = 0, len(matrix)-1
        while bottom > up:
            matrix[up], matrix[bottom] = matrix[bottom], matrix[up]
            up += 1
            bottom -= 1
        for i in range(len(matrix)):
            for j in range(0,i,1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return 
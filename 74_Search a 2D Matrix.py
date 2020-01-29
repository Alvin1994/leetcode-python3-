class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        left, right = 0, len(matrix) - 1
        while left <= right:
            m = (left + right) // 2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] < target:
                left = m + 1
            else: 
                right = m - 1
        head, left, right = left - 1, 0, len(matrix[left - 1]) - 1
        while left <= right:
            m = (left + right) // 2 
            if matrix[head][m] == target:
                return True
            if matrix[head][m] < target:
                left = m + 1
            else:
                right = m - 1
        return False
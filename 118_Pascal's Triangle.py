class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        if numRows<1:
            return []
        rst = []
        if numRows == 1:
            rst.append([1])
        elif numRows == 2:
            rst.append([1])
            rst.append([1,1])
        else:
            rst.append([1])
            rst.append([1,1])
            for level in range(2,numRows,1):
                if len(rst) < level+1:
                    rst.append([1])
                for i in range(level-1):
                    rst[level].append(rst[level-1][i]+rst[level-1][i+1])
                rst[level].append(1)        
        return rst
        
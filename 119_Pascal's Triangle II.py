class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex < 0 or  rowIndex>34:
            return []    
        
        rst = [1]
        for _ in range(rowIndex):
            rst = [x+y for x,y in zip([0]+rst,rst+[0])]
        return rst
        
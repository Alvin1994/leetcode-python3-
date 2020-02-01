class Solution:
    # bottom up
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        if not triangle:
            return 
        
        rst = triangle[-1]
        for level in range(len(triangle)-2,-1,-1):
            for i in range(0,len(triangle[level]),1):
                rst[i] = triangle[level][i] + min(rst[i], rst[i+1])
        return rst[0]
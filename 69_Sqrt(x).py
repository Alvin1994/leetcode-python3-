class Solution:
    def mySqrt(self, x: int) -> int:
        assert isinstance(x, int)
        
        if x== 0:
            return 0
    
        l,r = 0, x
        while r >= l:
            mid = (r+l) // 2
            
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            if x < mid*mid:
                r = mid - 1
            else:
                l = mid + 1
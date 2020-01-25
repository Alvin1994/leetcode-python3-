class Solution:
    def myPow(self, x: 'float', n: 'int') -> 'float':
        assert isinstance(x,float) and isinstance(n,int)
        def helper(x,n):
            if n == 0:
                return 1
            half = helper(x,int(n/2))
            if n % 2 == 0:
                return half*half
            else:
                return half*half*x
            
        if n >= 0:
            return helper(x,n)
        else:
            return 1/helper(x,-n)
    
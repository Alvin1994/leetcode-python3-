class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        assert isinstance(n, int) and isinstance(k, int)
        
        nums = [str(x+1) for x in range(n)]
        fact = [1] * n
        for i in range(1,n,1):
            fact[i] = i * fact[i-1]
        k -= 1
        rst = ""
        for i in range(n,0,-1):
            index = k // fact[i-1]
            print(k, fact[i-1], index)
            rst += nums.pop(index)
            k %= fact[i-1]
        return rst
    
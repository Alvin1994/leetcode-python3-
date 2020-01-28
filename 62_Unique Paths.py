class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        assert isinstance(m, int) and isinstance(n, int)
        
        if m <= 0 or n <= 0:
            return 
        permutation = m + n - 2
        fact = [1] * (permutation + 1)
        i = 1
        while i <= permutation :
            fact[i] = i * fact[i-1]
            i += 1
        return fact[permutation] // (fact[m - 1] * fact[n - 1])
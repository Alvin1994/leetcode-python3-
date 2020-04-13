class Solution:
    def trailingZeroes(self, n: int) -> int:
        rst = 0
        while n > 0:
            rst += n // 5
            n //= 5
        return rst
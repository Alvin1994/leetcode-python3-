class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        intMax = 2**31-1
        intMin = -2**31
        rev = 0
        sign = 1
        if x > intMax or x < intMin:
            return 0
        if x < 0:
            sign = -1
            x *= sign 
        while x != 0:
            pop = x % 10
            x = int(x/10)
            rev = rev * 10 + pop
        return 0 if rev>intMax or rev<intMin else rev*sign
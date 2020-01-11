class Solution:
    def isPalindrome2(self, x: int) -> bool:
        assert isinstance(x,int)
        
        if x < 0:
            return False
        
        def is_palindrome(l,r,s):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -=1
                r +=1
            return r-l-1
        s = str(x)
        i = (len(s)-1) // 2
        max_len = max(is_palindrome(i,i,s),is_palindrome(i,i+1,s))
        return max_len == len(s)
    def isPalindrome(self, x: int) -> bool:
        assert isinstance(x,int)
        
        if x < 0:
            return False
        
        copy_x = copy.copy(x)
        rev = 0
        while copy_x !=0:
            rev = rev*10 + copy_x%10
            copy_x = copy_x //10
        return rev == x
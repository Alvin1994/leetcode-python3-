class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: strY  
        """
        assert isinstance(s,str)
        
        def expand_from_center(l,r,s):    
            while l >=0 and r < len(s) and s[l] == s[r]:
                l = l-1
                r = r+1
            return r-l-1
        l=r=0
        for i in range(len(s)):
            max_len = max(expand_from_center(i,i,s), expand_from_center(i,i+1,s))
            if max_len > r - l+1:
                l = i - int((max_len-1)//2)
                r = i + int(max_len//2)
        return s[l:r+1]
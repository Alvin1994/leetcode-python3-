class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        assert isinstance(s,str)
        
        if not s:
            return 0
        i = len(s)-1
        
        while i>=0 and s[i] == ' ':
            i -= 1
        rst = 0
        while i>=0 and s[i] != ' ':
            rst += 1
            i -= 1
        return rst
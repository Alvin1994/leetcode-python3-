class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        assert isinstance(s,str)
        
        l,r = -1,0
        str_position = dict()
        max_len = 0
        while r < len(s):
            curt_str = s[r]
            
            if curt_str in str_position and l < str_position[curt_str]:
                l = str_position[curt_str]
                str_position[curt_str] = r
            else:
                str_position[curt_str] = r
                max_len = max(max_len,r-l)
            r+=1
        return max_len

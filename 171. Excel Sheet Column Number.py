class Solution:
    # @return an int
    def titleToNumber(self, s: str) -> int:
        maps = {}
        for i, capital in enumerate(string.ascii_uppercase):
            maps[capital] = i + 1
        res = 0
        i = 0
        while i < len(s):
            res = res * 26 + maps[s[i]]
            i += 1
        return res
            
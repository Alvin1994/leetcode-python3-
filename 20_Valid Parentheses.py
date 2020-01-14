class Solution:
    def isValid(self, s: str) -> bool:
        assert isinstance(s,str)
        
        mapping = {')':'(',']':'[','}':'{'}
        stack = []
        for s_ in s:
            if s_ in mapping:
                if not stack or mapping[s_] != stack.pop():
                    return False
            else:
                stack.append(s_)
        return False if stack else True
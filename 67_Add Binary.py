class Solution:
    def addBinary(self, a: str, b: str) -> str:
        assert isinstance(a, str) and isinstance(b, str)
        
        if not a or not b:
            return a if a else b
        a = list(a)
        b = list(b)
        
        c = 0
        rst = ""
        while a or b or c:
            if a:
                c += int(a.pop())
            if b:
                c += int(b.pop())
            rst = str(c % 2) + rst
            c //= 2
        return rst
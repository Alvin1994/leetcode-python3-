class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return ""
        return self.countAndSay_(n)
        
    def countAndSay_(self, n: int) -> str:
        
        if n == 1:
            return "1"
        str_ = self.countAndSay_(n-1)
        rst = ""
        i = 0
        val, count = str_[0], 0
        while i<len(str_):
            if str_[i] != val:
                rst += str(count)
                rst += str(val)
                val, count = str_[i], 1
            else:
                count += 1
            i += 1
        rst += str(count)
        rst += str(val)
        return rst
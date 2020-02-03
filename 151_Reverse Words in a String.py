class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        # 1. remove space front and tail side # 2. revised all string,  # 3. revise words 
        def revised(s,l,r):
            s = list(s)
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1 
                r -= 1
            return "".join(s)
        
        def remove_space(s):
            s = list(s)
            i = 0
            while i<len(s)-1:
                if s[i] == " " and s[i+1] == " ":
                    s.pop(i+1)
                    continue
                i += 1
            if s[0] == " ":
                s.pop(0)
            if not s:
                return ""
            if s[-1] == " ":
                s.pop()
            return "".join(s)
        # 1. remove space
        s = remove_space(s)
        
        # 2. 
        s = revised(s,0,len(s)-1)
        
        # 3.
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == " ":
                i += 1
            if i == len(s):
                break
            j = i + 1
            while j < len(s) and s[j] != " ":
                j += 1
            s = revised(s,i,j-1)
            i = j + 1
        
        return s
        
        
#     def reverseWords(self, s: str) -> str:
#         if not s:
#             return ""
#         rst = []
#         l = 0
#         while l < len(s):
#             while l < len(s) and s[l] == " ":
#                 l += 1
#             if l == len(s):
#                 break
#             r = l + 1
#             while r < len(s) and s[r] != " ":
#                 r += 1
#             rst.insert(0,s[l:r])
#             l = r + 1
#         return  " ".join(rst)
        
        
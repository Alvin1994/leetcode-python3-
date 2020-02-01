class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        if not s:
            return []
        
        def helper(l,r,path,rst):
            if l > r:
                return rst.append(path)
            for i in range(l,r+1,1):
                strs = s[l:i+1]
                if strs==strs[::-1]:
                    helper(i+1,r,path+[s[l:i+1]],rst)
        
        rst = []
        helper(0,len(s)-1,[],rst)
        return rst
    
    
#     def _partition(self,s:'str',path:'List',rst:'List') -> None:
#         def isPalindrome(s:'str') -> 'bool':
#             return s == s[::-1]
#         if not s:
#             rst.append(path)
#         for i in range(1,len(s)+1,1):
#             if isPalindrome(s[:i]):
#                 self._partition(s[i:], path + [s[:i]], rst)
        
        
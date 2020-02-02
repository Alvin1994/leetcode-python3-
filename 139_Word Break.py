class Solution:
    def wordBreak(self,s:'str', words:'list') -> 'bool':
        
        if not s or not words:
            return False
        memo = dict()
        def helper(l,r):
            if l > r:
                return True
            if s[l:r+1] in memo:
                return False
            for i in range(l,r+1,1):
                if s[l:i+1] in words:
                    if helper(i+1,r):
                        return True
            memo[s[l:r+1]] = False
            return False
        return helper(0,len(s)-1)
#     # Dynatic programming
#     def wordBreak(self,s:'str', words:'list') -> 'bool':
#         if not s or not words:
#             return False
#         dp = [False for i in range(len(s)+1)]
#         dp[0] = True
#         for i in range(1,len(s)+1,1):
#             for word in words:
#                 print(i-len(word))
#                 print(dp[i-len(word)])
#                 if dp[i-len(word)] and s[i-len(word):i] in words:
#                     dp[i] = True
#         return dp[-1]            
          

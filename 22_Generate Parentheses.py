class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        assert isinstance(n,int) and n > 0
        self.map = dict()
        def dfs(n):
            if n in self.map:
                return self.map[n]
            if n == 1:
                self.map[1] = ['()']
                return ['()']
            
            ans = set()
            
            for item in dfs(n-1):
                ans.add('(' + item + ')')
                
            for i in range(1, n//2 + 1):
                for left in dfs(i):
                    for right in dfs(n-i):
                        ans.add(left + right)
                        ans.add(right + left)
            self.map[n] = ans
            return self.map[n]

        return dfs(n)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        assert isinstance(board, list) and isinstance(word, str)
        
        if not board or not word:
            return False
        def dfs(i,r,c):
            if i == len(word):
                return True
            if r<0 or c<0 or r >= len(board) or c >= len(board[0]):
                return False
            if board[r][c] == word[i]:
                tmp = board[r][c]
                board[r][c] = '#'
                rst =  dfs(i+1, r-1,c) or dfs(i+1, r+1,c) or dfs(i+1, r,c-1) or dfs(i+1, r,c+1)
                board[r][c] = tmp
                return rst
            return False
        i = 0
        
        for r in range(0,len(board), 1):
            for c in range(0, len(board[0]), 1):
                if dfs(i,r,c):
                    return True
        return False
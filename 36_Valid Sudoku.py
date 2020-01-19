class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]:
            return 
        tmp = []
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    tmp += [(board[r][c], r), (c,board[r][c]), (r//3,c//3,board[r][c])]

        return len(tmp)==len(set(tmp))
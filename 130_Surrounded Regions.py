class Solution:
    def solve(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        stack = []
        
        # check on board 
        for row in [0,len(board)-1]:
            for col in range(len(board[row])):
                if board[row][col] == 'O':
                    stack.append((row,col))
                    
        for col in [0, len(board[0])-1]:
            for row in range(1,len(board)-1,1):
                if board[row][col] == 'O':
                    stack.append((row,col))
                    
        # DFS 
        while stack:
            row, col = stack.pop()
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
                board[row][col] ='F'
                stack.append((row,col+1))
                stack.append((row,col-1))
                stack.append((row+1,col))
                stack.append((row-1,col))
        # cover
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'F':
                    board[row][col] = 'O'
        return None
                               
                               
                               
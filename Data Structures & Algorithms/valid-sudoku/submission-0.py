from collections import defaultdict

class Solution:
    def validRows(self, board):
        # rows
        temp_row = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in temp_row[i]:
                    return False
                    
                temp_row[i].add(board[i][j])
        return True


    def validColumns(self, board):
        # cols
        temp_col = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in temp_col[j]:
                    return False
                
                temp_col[j].add(board[i][j])
                
        return True


    def validBlocks(self, board):
        # blocks
        temp_block = defaultdict(set)
        for i in range(9):
            
            for j in range(9):
                block = (i//3) * 3 + (j//3)
                
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in temp_block[block]:
                    return False
                
                temp_block[block].add(board[i][j])
                
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
        self.validRows(board) and 
        self.validColumns(board) and
        self.validBlocks(board)
        )
        
            
        
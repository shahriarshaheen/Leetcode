class Solution(object):
    def isValidSudoku(self, board):
        for r_row in range(9):
            row_seen=set()
            for r_col in range(9):
                val=board[r_row][r_col]
                if val==".":
                    continue
                if val in row_seen:
                    return False
                else:
                    row_seen.add(val)
        for c_col in range(9):
            col_seen=set()
            for c_row in range(9):
                val=board[c_row][c_col]
                if val==".":
                    continue
                if val in col_seen:
                    return False
                else:
                    col_seen.add(val)
        
        for square in range(9):
            square_seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    col=(square%3)*3+j
                    val=board[row][col]
                    if val==".":
                        continue
                    if val in square_seen:
                        return False
                    else:
                        square_seen.add(val)
        return True
        
        
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(self, board) -> bool:
    for i in range(9) :
        for k in range(9) :
            if (board[i][k] != ".") :
                for j in range(9) :
                    if ((board[i][k] == board[i][j] and k != j) or (board[i][k] == board[j][k] and i != j)) :
                        return False
                for j in range((k // 3)*3,(((k // 3) + 1)*3)) :
                    for t in range((i // 3)*3,(((i // 3) + 1)*3)) :
                        if ((board[i][k] == board[t][j]) and (i != t) and (k != j)) :
                            return False
    return True
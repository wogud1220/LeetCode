class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = []
        for i in range(9):
            arr = []
            for j in range(9):
                if (board[i][j] in arr) and (board[i][j] != '.'):
                    return False
                else:
                    arr.append(board[i][j])


        for j in range(9):
            arr = []
            for i in range(9):
                if (board[i][j] in arr) and (board[i][j] != '.'):
                    return False
                else:
                    arr.append(board[i][j])
            
        for t in range(9):
            arr = []
            row = (t // 3) * 3
            col = (t % 3) * 3

            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j] != '.':
                        arr.append(board[row+i][col+j])

            if len(arr) != len(set(arr)):
                return False


        return True
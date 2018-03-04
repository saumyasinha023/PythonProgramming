class Solution():
    def isValidSudoku(self, board):
        for i in range(9):
            row = set()
            column = set()
            cube = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in column:
                        return False
                    else:
                        column.add(board[j][i])
                rowIndex = int(3 * (i / 3))
                colIndex = int(3 * (i % 3))
                if board[rowIndex + int(j / 3)][colIndex + int(j % 3)] != '.':
                    if board[rowIndex + int(j / 3)][colIndex + int(j % 3)] in cube:
                        return False
                    else:
                        cube.add(board[rowIndex + int(j / 3)][colIndex + int(j % 3)])
            return True


S = Solution()
out = S.isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."],
                       ["4", ".", "3", ".", ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."],
                       [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", ".", "."]])
print(out)

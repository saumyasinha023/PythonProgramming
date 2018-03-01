class Solution():
    def solve(self, board):
        if board==None or board==[]:
            return None
        tmpBoard = [["X" for every in range(len(board[0]))] for each in range(len(board))]
        print(len(board),len(board[0]))
        for each in range(len(board)):
            for every in range(len(board[0])):
                if board[each][every] == 'O' and (each == 0 or each == len(board)-1 or every==0 or every==len(board[0])-1):
                    self.helperCapture(board, tmpBoard, each, every)
        board=tmpBoard
        print(board)

    def helperCapture(self, board, tmpBoard, each, every):
        if  each < 0 or every <0 or each >=len(board) or every>=len(board[0]) or board[each][every] == 'X' or tmpBoard[each][every]=='O':
            return
        tmpBoard[each][every] = 'O'
        self.helperCapture(board, tmpBoard, each - 1, every)
        self.helperCapture(board, tmpBoard, each + 1, every)
        self.helperCapture(board, tmpBoard, each, every - 1)
        self.helperCapture(board, tmpBoard, each, every + 1)




S = Solution()
S.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])

# [["X","X","X","X","X"],
#  ["X","O","O","X","X"],
#  ["X","X","O","X","X"],
#  ["X","O","X","X","X"]]

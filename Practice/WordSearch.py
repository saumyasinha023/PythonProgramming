class Solution(object):
    def exist(self, board, word):

        if board is None:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        if len(word)==0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'

        res = self.dfs(board, word[1:], i + 1, j) or self.dfs(board, word[1:], i - 1, j) or \
              self.dfs(board, word[1:], i, j + 1) or self.dfs(board, word[1:], i, j - 1)
        board[i][j] = tmp
        return res


board = [["a"]]
S = Solution()
print(S.exist(board, word="ab"))

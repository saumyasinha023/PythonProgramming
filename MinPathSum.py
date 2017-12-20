import sys


class Solution():
    def findminpathsum(self, grid, trace, i, j):
        x = [1, 0]
        y = [0, 1]
        ans = 0

        if i > len(grid) - 1 or j > len(grid[0]) - 1:
            return sys.maxsize
        if trace[i][j]:
            return trace[i][j]
        if i == len(grid)-1 and j == len(grid[0]) - 1:
            return grid[i][j]
        ans = min(grid[i][j] + self.findminpathsum(grid, trace, i + x[0], j + y[0]),
                  grid[i][j] + self.findminpathsum(grid, trace, i + x[1], j + y[1]))
        trace[i][j]=ans
        return ans

    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        trace = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        sum = self.findminpathsum(grid, trace, i=0, j=0)

        return sum


S = Solution()
print(S.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

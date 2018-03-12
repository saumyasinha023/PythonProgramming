from collections import deque


class Solution(object):
    def updateMatrix(self, matrix):
        if not matrix:
            return matrix

        result = [[None for j in range(len(matrix[0]))] for i in range(len(matrix))]
        queue = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            i, j, dist = queue.popleft()

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and result[i][j] == None:
                queue.append((i + 1, j, dist + 1))
                queue.append((i, j + 1, dist + 1))
                queue.append((i, j - 1, dist + 1))
                queue.append((i - 1, j, dist + 1))
                result[i][j] = dist

        return (result)


S=Solution()
print(S.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
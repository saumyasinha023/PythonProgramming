class Solution():
    def spiralOrder(self, matrix):
        arr = []
        while matrix:
            arr += matrix.pop(0)
            if matrix and matrix[0]:
                for eachRow in matrix:
                    arr.append(eachRow.pop())
            if matrix:
                arr += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for eachRow in matrix[::-1]:
                    arr.append(eachRow.pop(0))
        return arr


S = Solution()
print(S.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

#
# [[1, 2, 3]
#  [4, 5, 6]
#  [7, 8, 9]]

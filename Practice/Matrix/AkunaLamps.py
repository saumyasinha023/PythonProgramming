class Solution():

    def num_illuminated(self, grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y):
        if start_x > grid_height or start_y > grid_width:
            return grid_height * grid_width
        matrix = [['L' for each in range(grid_height)] for every in range(grid_width)]
        arr = [(conn_x1, conn_y1), (conn_x2, conn_y2)]
        visited = []
        visited = self.helper(matrix, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y, visited)
        print((len(matrix) * len(matrix[0])) - len(visited))

    def helper(self, matrix, xcor, ycor, xcor2, ycor2, start_x, start_y, visited):
        if start_x >= len(matrix) or start_x < 0 or start_y >= len(matrix[0]) or start_y < 0 or matrix[start_x][
            start_y] != 'L':
            return
        matrix[start_x][start_y] = 'X'
        visited.append(1)
        self.helper(matrix, xcor, ycor, xcor2, ycor2, start_x + xcor, start_y + ycor, visited)
        self.helper(matrix, xcor, ycor, xcor2, ycor2, start_x + xcor2, start_y + ycor2, visited)
        return visited


# def num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y):
#     if grid_width == 0 and grid_height == 0:
#         return 0
#     if start_x > grid_width or start_y > grid_height:
#         return grid_height * grid_width
#     matrix = [['L' for each in range(grid_height)] for every in range(grid_width)]
#     arr = [(conn_x1, conn_y1), (conn_x2, conn_y2)]
#     visited = []
#
#     visited = helper(matrix, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y, visited)
#     if visited is None:
#         return 0
#     else:
#         return ((len(matrix) * len(matrix[0])) - len(visited))
#
#
# def helper(matrix, xcor, ycor, xcor2, ycor2, start_x, start_y, visited):
#     if start_x >= len(matrix) or start_x < 0 or start_y >= len(matrix[0]) or start_y < 0 or matrix[start_x][
#         start_y] != 'L':
#         return
#     matrix[start_x][start_y] = 'X'
#     visited.append(1)
#     helper(matrix, xcor, ycor, xcor2, ycor2, start_x + xcor, start_y + ycor, visited)
#     helper(matrix, xcor, ycor, xcor2, ycor2, start_x + xcor2, start_y + ycor2, visited)
#     return visited

S = Solution()
S.num_illuminated(5, 3, -1, 0, -1, -1, 4, 2)

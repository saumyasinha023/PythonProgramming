class Solution:
    def rotate(self, A):
        A[:] = map(list,zip(*A[::-1]))
        return A
A=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
S = Solution()
print(S.rotate(A))
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        if len(A) == 1:
            return 1

        mid = int(len(A) / 2)
        pos = mid
        if A[mid + 1] < A[mid]:
            return A[mid + 1]
        elif A[0] > A[len(A) - 1] and A[0] < A[mid]:
            while A[pos] >= A[mid] and pos < len(A) - 1:
                pos += 1
            return A[pos]
        else:
            while A[pos] <= A[mid] and pos > -1:
                pos -= 1
            return A[pos + 1]


A = [5137, 5525, 9511, 13269, 16255, 16700, 19870, 23034, 29247, 29934, 34583, 41585, 42598, 44113, 46035, 50147, 50737,
     57084, 65916, 76905, 84098, 85912, 92081, 92257, 95449]

S = Solution()
print(S.findMin(A))

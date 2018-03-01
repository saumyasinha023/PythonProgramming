class Solution:
    def generateParenthesis(self, n):
        str = ""
        arr = self.helper(1, 0, str + '(', n, arr=[])
        return arr

    def helper(self, open, close, str, n, arr):
        if len(str) == 2 * n:
            arr.append(str)
            return
        if open < n:
            self.helper(open + 1, close, str + '(', n, arr)
        if close < open:
            self.helper(open, close + 1, str + ')', n, arr)
        return arr

S=Solution()
print(S.generateParenthesis(3))
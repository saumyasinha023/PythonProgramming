class Solution(object):
    def findSum(self, arr):
        final = []
        maxi = 0
        for each in arr:
            sum = self.helper(each, arr, 0, 0)
            final.append(sum)

        for each in final:
            if each is None:
                continue
            if each > maxi:
                maxi = each
        print(maxi)

    def helper(self, each, arr, index, sum):
        if arr[index] == each:
            return
        sum = max(sum, each + arr[index])
        self.helper(each, arr, index + 1, sum)
        return sum


S = Solution()
S.findSum([1, 0, 3, 9, 2])

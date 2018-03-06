class Solution():
    def findPermutations(self, arr):
        tmp, final = [], []
        for each in range(len(arr[0])):
            final = self.helper(arr, [arr[0][each]], final, 1)
        print(final)

    def helper(self, arr, tmp, final, index):
        if len(tmp) == len(arr[0]):
            final.append(tmp)
        if index >= len(arr):
            return

        for every in range(len(arr[index])):
            self.helper(arr, tmp + [arr[index][every]], final, index + 1)
        return final


S = Solution()
S.findPermutations([[1, 2, 3], [4], [5, 6]])

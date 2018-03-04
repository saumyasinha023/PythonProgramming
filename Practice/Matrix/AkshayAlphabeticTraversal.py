class Solution():
    def traverse(self, mat):
        final, path = [], []
        self.helper(mat, final, path, 0, 0)
        print(final)

    def helper(self, mat, final, path, each, every):
        if each >= len(mat) or every >= len(mat[0]) or each < 0 or every < 0:
            return
        if each == len(mat) - 1 and every == len(mat[0]) - 1:
            final.append(path)

        self.helper(mat, final, path + ['H'], each, every + 1)
        self.helper(mat, final, path + ['V'], each + 1, every)

        return final


S = Solution()
S.traverse([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

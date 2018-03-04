class Solution(object):
    def longestSubstring(self, string):
        start = end = 0
        for each in range(len(string)):
            len1 = self.helper(string, each, each)
            len2 = self.helper(string, each, each + 1)
            maxi = max(len1, len2)

            if maxi >(end - start):
                start = int(each - (maxi - 1) / 2)
                end = int(each + maxi / 2)
        return string[start:end + 1]

    def helper(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1

        return right - left - 1


S = Solution()
print(S.longestSubstring("babad"))

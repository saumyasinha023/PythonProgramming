class Solution():
    def largestPalindrome(self, num):
        mid = len(num)
        i = mid - 1
        j = i - 1
        maxpos, minpos = 0, 0
        max, min = 0, 0

        while i > 0 and j > 0:
            if i < j:
                maxpos = j
                max = num[j]
                i = j
                j -= 1
            if j < i:
                minpos = j
                min = num[j]
                j -= 1
        if minpos < maxpos:
            return maxpos


S = Solution()
print(S.largestPalindrome(num=[4697557964]))

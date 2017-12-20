class Solution():
    def largestPalindrome(self, num):
        mid = len(num)
        i = mid - 1
        tmp = num[i]

        while i > 0:
            if num[i - 1] > num[i]:
                i = i - 1
        while j

S = Solution()
S.largestPalindrome(num=4697557964)

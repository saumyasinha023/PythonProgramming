class Solution():
    def Counter(self, nums, skips):
        skips -= 1
        i = 0
        while nums:
            i = (i + skips) % len(nums)
            print(nums[i], end="")
            nums.pop(i)


S = Solution()
S.Counter([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

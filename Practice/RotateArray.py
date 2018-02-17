class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 1234567
        # 5671234
        arr = []

        pos = 0
        if k > len(nums):
            k=k%len(nums)

        for i in range(k):
            arr.append(nums[i])
            if k > len(nums):
                break
        for i in range(len(nums) - 1, k - 1, -1):
            arr.insert(0, nums[i])

        nums = arr
        print(nums)

S = Solution()
S.rotate(nums=[1,2], k=1)

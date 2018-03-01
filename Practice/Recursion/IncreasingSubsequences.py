# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

class Solution():
    def findSubsequences(self,nums):
        if nums==None:
            return 0
        for each in range(len(nums)-1):
            if nums[each]>nums[each+1]:
                return []
        arr,final=[],[]
        return self.helper(nums,arr,final)


    def helper(self, nums, arr,final):
        if len(nums)<0:
            return
        if arr !=None and arr not in final and len(arr)>1:
            final.append(arr)

        for each in nums:
            self.helper(nums[nums.index(each)+1:],arr+[each],final)

        return final


S = Solution()
print(S.findSubsequences([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

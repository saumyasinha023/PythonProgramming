# [1,1,1,2,2,3] and k = 2, return [1,2]
#
# class Solution():
#
#     def topKFrequent(self,nums,k):
#         arr=[]
#         lenArr=max(nums)
#         tmpArr=[0 for each in range(lenArr)]
#         for each in nums:
#             tmpArr[each-1]+=1
#         for x in range(k):
#             arr.append(tmpArr.index(max(tmpArr[x:]))+1)
#         print(arr)
import heapq
from collections import defaultdict

#property of heapq is that smallest element is always the root

class Solution():

    def topKFrequent(self, nums, k):

        arr = []
        dictionary = defaultdict(int)
        heap = []
        for word in nums:
            dictionary[word] += 1

        for each in dictionary:
            heapq.heappush(heap, (-dictionary[each], each))
        print(heap)

        tmp = heap[k - 1][1]
        for each in range(len(nums)):
            if nums[each] == tmp:
                arr.append(each)

        print(arr)


S = Solution()
S.topKFrequent([1, 1, 1, 2, 2, 3,3,3,3,3], 1)

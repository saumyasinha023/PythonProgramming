# [1,1,1,2,2,3] and k = 2, return [1,2]

class Solution():

    def topKFrequent(self,nums,k):
        arr=[]
        lenArr=max(nums)
        tmpArr=[0 for each in range(lenArr)]
        for each in nums:
            tmpArr[each-1]+=1
        for x in range(k):
            arr.append(tmpArr.index(max(tmpArr[x:]))+1)
        return(arr)



S=Solution()
S.topKFrequent([1,1,1,2,2,3],2)
import heapq


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        arr=[]
        dictionary={}
        heap=[]
        for word in words:
            if word in dictionary:
                dictionary[word]+=1
            else:
                dictionary[word]=1

        for each in dictionary:
            heapq.heappush(heap,(-dictionary[each],each))

        for i in range(k):
            arr.append(heapq.heappop(heap)[1])

        return(arr)

S=Solution()
print(S.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"],k=2))
import heapq
from collections import defaultdict


class Solution():
    def arrange(self, word):
        dict = defaultdict(int)
        arr, heap = [], []

        for each in word:
            dict[each] += 1
        for each in dict:
            heapq.heappush(heap, (-dict[each], each))
        prev = (100000, '#')
        while heap:
            out = heap.pop(0)
            arr.append(out[1])
            if prev[0] < 0:
                heapq.heappush(heap, (prev[0], prev[1]))
            dict[out[1]] -= 1
            prev = (-dict[out[1]], out[1])

        print("".join(arr))


S = Solution()
S.arrange("aaabc")

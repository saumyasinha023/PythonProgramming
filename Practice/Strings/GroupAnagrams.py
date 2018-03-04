from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        dict = defaultdict(list)
        for each in strs:
            a = "".join(sorted(each))
            dict[a] += [each]

        arr = []
        for each in dict:
            arr.append(dict[each])
        print(arr)


S = Solution()
S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

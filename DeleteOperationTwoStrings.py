class Solution:
    def minDistance(self, word1, word2):
        """
        :param word1:
        :param word2:
        :return:
        """
        dict = {}
        count = 1
        for i in word1:
            if i not in dict:
                dict[i] = count
            else:
                count = dict[i] + 1
                dict[i] = count
        print(dict)

        count=1
        for i in word2:
            if i not in dict:
                dict[i] = count
            else:
                dict[i] = dict[i] + 1
        diff=0

        for i in dict:
            if dict[i]==1 or dict[i]%2==1:
                diff+=1
        return(int(diff))

S = Solution()
print(S.minDistance("sea", "ate"))

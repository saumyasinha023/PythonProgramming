class Solution(object):
    def calculate(self, count, i):
        if i == 1:
            return count
        else:
            count += 1
            return self.calculate(count, i - 1)

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        count = self.calculate(count, n)

        return count

S=Solution()
print(S.numTrees(3))
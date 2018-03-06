import random


class Solution():
    def __init__(self):
        self.weightSum = 0

    def preProcessor(self, w):
        for each in w:
            self.weightSum += w[each]

    def randomGenerator(self, w):
        sum = 0
        randInt = random.randint(1, self.weightSum)
        for each in w:
            sum += w[each]
            if sum >= randInt:
                return each


S = Solution()
S.preProcessor(w={'A': 1.0, 'B': 1.0, 'C': 1.0})
print(S.randomGenerator(w={'A': 1.0, 'B': 1.0, 'C': 1.0}))

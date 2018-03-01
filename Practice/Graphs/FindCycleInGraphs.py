from collections import defaultdict


class Solution():
    def __init__(self):
        self.g = {2: [0,3], 1: [2], 0: [2,1],}

    def detectCycle(self):
        string = "Has Cycle"
        stk, final = [], []
        for each in self.g:
            for every in self.g[each]:
                stk.append(every)

            for eachNode in stk:
                t = stk.pop()
                if t not in final:
                    final.append(t)
                else:
                    print(t)
                    return string

S = Solution()
print(S.detectCycle())

class Solution():
    def astroidCollision(self, list1):
        stk = []
        for each in list1:
            while stk and each < 0 < stk[-1]:
                if -each > stk[-1]:
                    stk.pop()
                    continue
                elif -each == stk[-1]:
                    stk.pop()
                break
            else:
                stk.append(each)
        return stk


S = Solution()
print(S.astroidCollision([5, 10, -5]))

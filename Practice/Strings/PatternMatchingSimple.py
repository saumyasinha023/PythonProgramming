class Solution(object):
    def isMatched(self, s, p):
        return self.dfs(s, 0, p, 0)

    def dfs(self,s, si, p, pi):
        while si < len(s) and pi < len(p) and s[si] == p[pi]:
            si += 1
            pi += 1
        if si == len(s) and pi == len(p):
            return True
        if pi < len(p) and p[pi] == "{":
            c = p[pi - 1]
            start = pi
            while pi < len(p) and p[pi] != "}":
                pi += 1
            left, right = map(int, p[start + 1:pi].split(","))
            for k in range(left, right):
                if s[si:si + k - 1] == c * (k - 1):
                    if self.dfs(s, si + k - 1, p, pi + 1):
                        return True
        return False


S = Solution()
print(S.isMatched("aaa", "aa{2,3}"))

class Solution():
    def matcher(self, arr):
        delimiters = ['{', '}', '(', ')', '[', ']']
        stk = []
        for each in arr:
            if each not in delimiters:
                continue
            else:
                if each == '(' or each == '[' or each == '{':
                    stk.append(each)

            if each == ')' and len(stk) >= 0:
                if len(stk) == 0: return False
                out = stk.pop()
                if out != '(' :
                    return False

            if each == '}' and len(stk) >= 0:
                if len(stk) == 0: return False
                out = stk.pop()
                if out != '{' :
                    return False

            if each == ']' and len(stk) >= 0:
                if len(stk)==0:return False
                out = stk.pop()
                if out != '[' :
                    return False
        if len(stk) != 0:
            return False
        return True


S = Solution()
print(S.matcher("]"))

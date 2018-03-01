# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


class Solution:
    def __init__(self):
        self.dict = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                     7: ['p', 'q', 'r', 's'],
                     8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        self.digits = None
    def letterCombinations(self, digits):
        if digits == None or digits == '':
            return []
        arrDigits, final = [], []
        self.digits = digits
        arr = ''
        for each in digits:
            arrDigits.append(int(each))
        final = self.helper(arr, final, 0, arrDigits)
        return final

    def helper(self, arr, final, index,arrDigits):
        if index >= len(self.digits):
            final.append(arr)
            return
        if arrDigits == None:
            return
        letters=self.dict[arrDigits[index]]
        for each in letters:
            self.helper(arr + each, final,index+1,arrDigits)
        return final


S = Solution()
print(S.letterCombinations('234'))

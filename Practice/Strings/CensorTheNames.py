class Solution():
    def censor(self,string,arr):
        tArr=[]

        for each in string.split():
            if each.lower() not in arr and each not in arr:
               tArr.append(each)
        print(tArr)
        print(" ".join(tArr))

S=Solution()
S.censor("Hi Sam my name is Saumya",["sam","saumya"])
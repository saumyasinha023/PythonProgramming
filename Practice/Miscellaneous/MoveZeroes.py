class Solution():
    def moveToRight(self, arr):
        tmp = []
        index = 0
        while index<len(arr):
            if arr[index] == 0:
                tmp.append(arr.pop(index))
            else:
                index += 1
        for each in tmp:
            arr.append(each)
        print(arr)

S = Solution()
S.moveToRight([1, 2, 0, 3, 0, 1, 2])

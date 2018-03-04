class Solution(object):
    def biggestNumber(self, num):
        num = sorted(num)

        arr = []
        for each in num[::-1]:
            arr.append(each)
        arr = "".join(arr)
        print(arr)

    def nextbiggestNumber(self, num):
        index, tIndex = 0, 0
        diff = 1000000000
        arr = []
        tNum = str(num)
        for each in tNum:
            arr.append(int(each))

        for each in range(len(arr) - 1, -1, -1):
            if arr[each - 1] < arr[each]:
                index = each - 1
        for i in range(len(arr) - 1, index, -1):
            if arr[i] > arr[index]:
                tIndex = i
                break

        arr[index], arr[tIndex] = arr[tIndex], arr[index]
        arr[index + 1:] = sorted(arr[index + 1:])

        print(arr)


S = Solution()
S.biggestNumber("62832")
S.nextbiggestNumber(63228)

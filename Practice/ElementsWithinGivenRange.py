class Solution():
    def __init__(self):
        self.lowerIndex = 0
        self.upperIndex = 0

    def inRange(self, arr, lowerLimit, upperLimit):
        arr = sorted(arr)
        mid = int((len(arr)-1) / 2)
        self.upperIndex=len(arr)-1

        leftIndex = self.helperRangeLeft(mid, arr, lowerLimit)
        rightIndex = self.helperRangeRight(mid + 1, arr, upperLimit)
        print(rightIndex - leftIndex + 1)

    def helperRangeLeft(self, mid, arr, lowerLimit):
        if mid <= 0:
            return self.lowerIndex
        if arr[mid] == lowerLimit:
            self.lowerIndex = mid
        self.helperRangeLeft(int(mid / 2), arr, lowerLimit)
        return self.lowerIndex

    def helperRangeRight(self, mid, arr, upperLimit):
        if mid+1 > len(arr)-1:
            return self.upperIndex
        if arr[mid] == upperLimit:
            self.upperIndex = mid
        self.helperRangeRight(int((mid + len(arr))/ 2), arr, upperLimit)
        return self.upperIndex


S = Solution()
S.inRange([1, 3, 4, 9, 10, 3], 9, 12)

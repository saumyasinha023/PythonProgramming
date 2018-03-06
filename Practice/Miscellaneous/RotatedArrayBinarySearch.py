class Solution():
    def findElement(self, arr, elem):

        return (self.helper(arr, elem, 0, len(arr) - 1))

    def helper(self, arr, elem, start, end):
        mid = int((start + end) / 2)
        if mid < 0 or mid > len(arr):
            return -1

        if arr[mid] == elem:
            return mid
        if arr[start] >= arr[mid]:
            if elem <= arr[end] and elem >= arr[mid]:
                return self.helper(arr, elem, mid + 1, end)
            return self.helper(arr, elem, start, mid - 1)
        if elem <= arr[end] and elem >= arr[mid + 1]:
            return self.helper(arr, elem, mid + 1, end)
        return self.helper(arr, elem, start, mid - 1)


S = Solution()
print(S.findElement([10, 20, 30, 3, 6, 7, 8], 7))

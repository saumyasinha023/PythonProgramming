class Solution(object):
    def multiply(self, num1, num2):
        a = len(num1)
        b = len(num2)
        x = num2
        for i in range(len(num1), -1, -1):
            val = num1 % 10
            num1 = int(num1 / 10)
            a[i] = val

            print(a)


S = Solution()
S.multiply(num1="12", num2="12")

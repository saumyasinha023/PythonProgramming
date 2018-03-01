class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):

        self.arr = self.arr[:len(self.arr)]

    def top(self):
        if len(self.arr) != 0:
            return (self.arr[len(self.arr) - 1])
        else:
            return 0

    def getMin(self):
        if len(self.arr) > 0:
            return min(self.arr)
        else:
            return 0


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(9)
# obj.push(8)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)
print(obj.arr)

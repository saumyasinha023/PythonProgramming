class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Tree(3)
root.left = Tree(1)
root.right = Tree(5)
root.left.left = Tree(0)
root.left.right = Tree(3)
root.right.left = Tree(3)
root.right.right = Tree(6)


class Solution:
    def __init__(self):
        self.arr = None
        self.height = None

    def averageOfLevels(self, root):
        self.arr = []
        self.helper(root, 0)
        print(self.arr)
        for each in range(len(self.arr)):
            self.arr[each]=self.mean(self.arr[each])
        return self.arr

    def helper(self, root, height):
        if root is None:
            return
        else:
            if len(self.arr) > height:
                self.arr[height].append(root.val)

            else:
                self.arr.append([root.val])
            self.helper(root.left, height + 1)
            self.helper(root.right, height + 1)

    def mean(self, numbers):
        return float(sum(numbers)) / max(len(numbers), 1)


S = Solution()
print(S.averageOfLevels(root))

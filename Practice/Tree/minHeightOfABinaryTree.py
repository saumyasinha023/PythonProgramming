class Tree(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution():
    def minDepth(self, root):
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1)


root = Tree(1)
root.left = Tree(2)
# root.right = Tree(3)
S = Solution()
print(S.minDepth(root))

class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Tree(3)
root.left=Tree(9)
root.right=Tree(20)
root.right.left=Tree(15)
root.right.right=Tree(7)


class Solution():
    def invertTree(self,root):
        if root is None:
            return
        else:
            # important concept
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

S=Solution()
first=S.invertTree(root)
print(first.left.val,first.right.val,first.left.left.val,first.left.right.val)
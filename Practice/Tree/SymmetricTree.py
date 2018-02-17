
class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Tree(1)
root.left = Tree(2)
root.right = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(4)
root.right.left = Tree(4)
root.right.right = Tree(3)

class Solution():

    def checkSymmetry(self,left, right):
        if left==None or right==None:
            return left==right
        if left.val!=right.val:
            return False
        return self.checkSymmetry(left.left,right.right) and self.checkSymmetry(left.right,right.left)


    def isSymmetric(self,root):
        if root==None:
            return True
        else:
            return self.checkSymmetry(root.left,root.right)

S=Solution()
print(S.isSymmetric(root))
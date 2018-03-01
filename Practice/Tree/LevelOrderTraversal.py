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
    def __init__(self):
        self.arr=None
    def levelOrder(self, root):
        self.arr=[]
        self.levelHelper(root,0)
        return self.arr

    def levelHelper(self, root, height):
        if root is None:
            return
        if len(self.arr) > height:
            self.arr[height].append(root.val)
        else:
            self.arr.append([root.val])
        self.levelHelper(root.left,height+1)
        self.levelHelper(root.right,height+1)



S=Solution()
print(S.levelOrder(root))
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
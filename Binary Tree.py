class Tree(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

print(root.left.data)
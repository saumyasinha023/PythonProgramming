class Tree(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

root = Tree(5)
root.left = Tree(2)
root.right = Tree(7)
root.left.left = Tree(1)
root.left.right = Tree(3)
root.right.left = Tree(6)
root.right.right = Tree(8)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

    
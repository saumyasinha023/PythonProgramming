# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.diameter = None

    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        else:
            option1 = self.height(root.left) + self.height(root.right)
            option2 = self.diameterOfBinaryTree(root.left)
            option3 = self.diameterOfBinaryTree(root.right)
            option4 = max(option1, max(option2, option3))
        return option4

    def height(self, root):
        if root is None:
            return 0
        else:
            lh = self.height(root.left)
            rh = self.height(root.right)
            h = 1 + max(lh, rh)
        return h
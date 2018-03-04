class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def isBalanced(self, root):
        return (self.helper(root)!=-1)

    def helper(self, root):

        if root == None:
            return 0
        leftHeight = int(self.helper(root.left))
        if leftHeight == -1:
            return -1
        rightHeight = int(self.helper(root.right))
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right.right.right = TreeNode(4)
# root.right.left = TreeNode(2)

S = Solution()
print(S.isBalanced(root))

# Inorder sequence: D B E A F C
# Preorder sequence: A B D E C F

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root


S = Solution()
node = S.buildTree(preorder=['A', 'B', 'D', 'E', 'C', 'F'], inorder=['D', 'B', 'E', 'A', 'F', 'C'])
print(node.val, node.left.val, node.right.val)

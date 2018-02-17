

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind + 1:],postorder)
            root.left = self.buildTree(inorder[:ind],postorder)
            return root


S = Solution()
node = S.buildTree(inorder=[4, 8, 2, 5, 1, 6, 3, 7], postorder=[8, 4, 5, 2, 6, 7, 3, 1])
print(node.val, node.left.val, node.right.val)

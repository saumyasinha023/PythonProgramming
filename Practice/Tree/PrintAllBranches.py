class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


class Solution():
    def branches(self, node):
        path = []
        self.helper(node, path+[node.val])

    def helper(self, node, path):

        if node is None:
            return
        # path.append(node.val)
        if node.left is None and node.right is None:

            print(path)
            # path.pop(path.index(node.val))
            return

        self.helper(node.left, path+[node.left.val])
        self.helper(node.right, path+[node.right.val])


S = Solution()
S.branches(root)

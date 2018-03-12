# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def findTarget(self, root, k):

        return self.helper(root, k, {})

    def helper(self, root, k, store):
        val = None
        if root is None:
            return None
        if root.val==k:
            return True
        subtractedValue = k - root.val

        if subtractedValue not in store:
            store[root.val] = subtractedValue
        else:
            val = root.val
            return True

        return self.helper(root.left, k, store) or self.helper(root.right, k, store)







root = TreeNode(0)
root.left = TreeNode(-1)
root.right = TreeNode(2)
root.left.left = TreeNode(-3)
# root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

S = Solution()
print(S.findTarget(root, -4))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(1)
# root.right.right = TreeNode(11)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(1)
# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(-2)


class Solution:
    def pathSum(self, root, sum):
        if root is None :
            return 0
        arr,branches=[],[]
        branches=self.helper(root,sum,arr+[root.val],[])
        if branches is not None:
            return len(branches)
        return 1

    def helper(self, root, sum, arr, branches):
        tmp=0
        if root==None :
            return
        for each in arr[::-1]:
            tmp+=each
            if tmp>sum:
                continue
            if tmp==sum:
                branches.append(1)
        if root.left:
            self.helper(root.left,sum,arr+[root.left.val],branches)
        if root.right:
            self.helper(root.right,sum,arr+[root.right.val],branches)
        return branches


S = Solution()
print(S.pathSum(root,1))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        level=0
        if root==None:
            return None
        arr=[]
        val=[]
        self.helper(root,arr,val,level)
        return val

    def helper(self, node, arr,val,level):
        if node==None:
            return
        localLevel=level+1
        if localLevel not in arr:
            arr.append(localLevel)
            val.append(node.val)
        self.helper(node.right,arr,val,localLevel)
        self.helper(node.left, arr, val, localLevel)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
root.right.right=TreeNode(4)

S=Solution()
print(S.rightSideView(root))
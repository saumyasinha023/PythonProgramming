# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root==None:
            return
        self.helper(root.left,root.right)

    def helper(self, left, right):
        if left==None:
            return None
        left.next=right
        self.helper(left.left,left,right)
        self.helper(right.left,right.right)
        self.helper(left.right,right.left)



root=TreeLinkNode(0)
root.left=TreeLinkNode(1)
root.right=TreeLinkNode(2)
root.left.left=TreeLinkNode(3)
root.left.right=TreeLinkNode(4)
root.right.left=TreeLinkNode(5)
root.right.right=TreeLinkNode(6)

S=Solution()
S.connect(root)
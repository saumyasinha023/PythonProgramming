class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

#
# class Solution(object):
#     def __init__(self, num):
#         self.count = num
#
#     def kthSmallest(self, root):
#         if root is None:
#             return root
#         else:
#             self.kthSmallest(root.left)
#             self.count -= 1
#             if self.count == 0:
#                 print(root.val)
#             self.kthSmallest(root.right)


class Solution(object):
    global num

    def kthSmallest(self, root, k):
        global num
        num = k
        return self.helper(root)

    def helper(self, root):
        global num
        if root is None:
            return root
        a= self.helper(root.left)
        num -= 1
        if num == 0:
            return (root.val)
        b= self.helper(root.right)

        return (a or b)

S = Solution()
print(S.kthSmallest(root,3))

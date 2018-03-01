class TreeNode(object):
    def __init__(self, char):
        self.val = char
        self.left = None
        self.right = None


root = TreeNode('c')
root.left = TreeNode('b')
root.left.right = TreeNode('z')
root.left.left = TreeNode('a')
root.right = TreeNode('d')
root.right.right = TreeNode('e')


class Solution():

    def __init__(self):
        self.str = ""

    def generateString(self, root):
        if root == None:
            return root
        root.left = self.generateString(root.left)
        self.str += root.val
        root.right = self.generateString(root.right)
        return self.str
    #
    # def generateTree(self, string, start, end):
    #     # giveninordertraversal
    #     if start>end:
    #         return
    #     if start==end:
    #         return TreeNode(string)
    #     mid = int((end-start) / 2)
    #     node = TreeNode(string[mid])
    #
    #     node.left = self.generateTree(string, start, mid - 1)
    #     node.right = self.generateTree(string, mid+1, end - 1)
    #
    #     return node

    # def helper(self, string, root, mid):
    #
    #     if mid < 0 or mid >= len(string):
    #         return
    #     if root == None:
    #         root = TreeNode(string[mid])
    #
    #     if len(string) > 1:
    #         root.left = self.helper(string[:mid], root.left, int(len(string[:mid]) / 2))
    #         root.right = self.helper(string[mid + 1:len(string) - 1], root.right,
    #                                  int(len(string[mid + 1:len(string) - 1]) / 2))
    #     return root


S = Solution()
print(S.generateString(root))
# node = (S.generateTree("abzcde", 0, 5))
# print(node.val)

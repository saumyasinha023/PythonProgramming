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
    def findRoot(self, arr):
        visited, tmp = [], []
        for each in arr:
            visited = self.helper(each, arr, visited)
        return visited

    def helper(self, each, arr, visited):
        if root.right == None and root.left == None:
            return

        if each.left in arr and each.left not in visited:
            visited.append(each.left)
            self.helper(each.left, arr, visited)
        if each.right in arr and each.right not in visited:
            visited.append(each.right)
            self.helper(each.right, arr, visited)
        return visited


S = Solution()
node = (S.findRoot(arr=[root.left, root, root.left.right, root.left.left, root.right, root.right.right]))
print(len(node))

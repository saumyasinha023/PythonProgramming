class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
# root.right.left = Tree(None)
root.right.right = TreeNode(9)


class Solution(object):
    def counter(self, current):
        arr = []
        i, j = 0, len(current) - 1
        for vals in current:
            arr.append(vals.val)

        print(arr)
        if arr[i] is None:
            while arr[i] == None:
                i += 1
        if arr[j] is None:
            while arr[j] == None:
                j -= 1

        return (j - i + 1)

    def widthOfBinaryTree(self, root):
        if root is None:
            return 0

        count, tcount = 0, 0
        result, current, level = [], [root], 1
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)

                if node.left:
                    next_level.append(node.left)
                else:
                    node.left=TreeNode(None)
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                else:
                    node.right=TreeNode(None)
                    next_level.append(node.right)
            tcount = self.counter(current)
            count = max(tcount, count)
            current = next_level
        return count


S = Solution()
print(S.widthOfBinaryTree(root))

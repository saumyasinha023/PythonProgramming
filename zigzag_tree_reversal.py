class Tree(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

root = Tree(5)
root.left = Tree(2)
root.right = Tree(7)
root.left.left = Tree(1)
root.left.right = Tree(3)
root.right.left = Tree(6)
root.right.right = Tree(8)

class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return None

        result, current, level = [], [root], 1
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.data)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level % 2:
                result.append(vals)
            else:
                result.append(vals[::-1])
            level += 1
            current = next_level
        return result




S = Solution()
print(S.zigzagLevelOrder(root))

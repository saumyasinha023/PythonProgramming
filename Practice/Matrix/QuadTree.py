class TreeNode():
    def __init__(self, val):
        self.val = val
        self.one = None
        self.two = None
        self.three = None
        self.four = None


class SOlution():
    def quadTree(self, matrix):
        root = TreeNode(0)
        half = int((len(matrix) - 1) / 2)
        for eachRow in range(0, half + 1):
            tmp = matrix.pop(0)
            mid = int((len(tmp) - 1) / 2)
            for each in tmp[:mid + 1]:
                if root.one != None:
                    root.one += [each]
                else:
                    root.one = [each]
            for each in tmp[mid + 1:]:
                if root.two != None:
                    root.two += [each]
                else:
                    root.two = [each]
        for eachRow in range(0, len(matrix)):
            tmp = matrix.pop(0)
            mid = int((len(tmp) - 1) / 2)
            for each in tmp[:mid + 1]:
                if root.three != None:
                    root.three += [each]
                else:
                    root.three = [each]
            for each in tmp[mid + 1:]:
                if root.four != None:
                    if root.four[-1] == each:
                        continue
                    else:
                        root.four += [each]
                else:
                    root.four = [each]

        print(root.one, root.two, root.three, root.four)


S = SOlution()
S.quadTree([[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 5, 5],
            [9, 1, 5, 5]])

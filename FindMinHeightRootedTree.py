class Solution():
    def findMinHeightTrees(self, n, edges):
        nodes=[set() for _ in range(n)]
        for i,j in edges:
            nodes[i].add(j)
            nodes[j].add(i)
        print(nodes)

        leaves = []

        for i in range(len(nodes)):
            if len(nodes[i])==1:
                leaves.append(i)


S=Solution()
print(S.findMinHeightTrees(n=7,edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [2,6]]))
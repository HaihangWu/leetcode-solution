class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        n = len(isConnected)

        # 初始化父节点数组，每个城市初始时都是自己的父节点
        parent = list(range(n))

        def find(x):
            """查找x的根节点"""
            if parent[x] != x:
                parent[x] = find(parent[x])  # 路径压缩
            return parent[x]

        def union(x, y):
            """合并x和y所在的集合"""
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX  # 将一个根指向另一个根

        # 遍历邻接矩阵，合并相连的城市
        for i in range(n):
            for j in range(i + 1, n):  # 只需要遍历上三角，避免重复
                if isConnected[i][j] == 1:
                    union(i, j)

        # 统计不同根节点的数量（即省份数量）
        provinces = len(set(find(i) for i in range(n)))
        return provinces
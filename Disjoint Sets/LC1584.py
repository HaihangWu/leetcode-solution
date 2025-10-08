class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)
        if n == 1:
            return 0

        # 1. 构建所有边 (i, j, weight)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        # 2. 按权重排序
        edges.sort()

        # 3. 并查集
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            parent[rootY] = rootX
            return True

        # 4. Kruskal
        total_cost = 0
        edges_used = 0
        for dist, u, v in edges:
            if union(u, v):
                total_cost += dist
                edges_used += 1
                if edges_used == n - 1:
                    break

        return total_cost

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        obstacle_coords = [[i, j]
                           for i in range(len(obstacleGrid))
                           for j in range(len(obstacleGrid[0]))
                           if obstacleGrid[i][j] == 1]

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mem = [[-1 for _ in range(n)] for _ in range(m)]

        for obstacle in obstacle_coords:
            mem[obstacle[0]][obstacle[1]] = 0

        obstacle_h = None
        for i in range(m):
            if obstacle_h is None and [i, 0] in obstacle_coords:
                obstacle_h = i
            if obstacle_h is not None:
                mem[i][0] = 0
            else:
                mem[i][0] = 1

        obstacle_v = None
        for j in range(n):
            if obstacle_v is None and [0, j] in obstacle_coords:
                obstacle_v = j
            if obstacle_v is not None:
                mem[0][j] = 0
            else:
                mem[0][j] = 1

        def dp(h, v):
            if mem[h][v] == -1:
                mem[h][v] = dp(h - 1, v) + dp(h, v - 1)
            return mem[h][v]

        return dp(m - 1, n - 1)
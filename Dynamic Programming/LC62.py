class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mem = [[-1 for _ in range(n)] for _ in range(m)]
        mem[0][0] = 1
        for i in range(m):
            mem[i][0] = 1
        for j in range(n):
            mem[0][j] = 1

        def dp(h, v):
            if mem[h][v] == -1:
                mem[h][v] = dp(h - 1, v) + dp(h, v - 1)
            return mem[h][v]

        return dp(m - 1, n - 1)


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        mem = [-1 for _ in range(n + 1)]

        def dfs(k):
            # base cases
            if k == 0:
                return 0

            if mem[k] != -1:
                return mem[k]

            res = dfs(k - 1) + 1
            val = int(math.sqrt(k))
            for i in range(2, val + 1):
                res = min(res, dfs(k - i * i) + 1)

            mem[k] = res

            return res

        return dfs(n)
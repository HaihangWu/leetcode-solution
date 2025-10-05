class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [-1] * (n + 1)
        mem[0] = 1
        mem[1] = 1

        def dfs(k):
            if mem[k] == -1:
                mem[k] = dfs(k - 2) + dfs(k - 1)
            return mem[k]

        return dfs(n)


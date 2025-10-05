class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        mem = [-1] * (n + 1)
        mem[0] = 0
        mem[1] = 0
        mem[2] = min(cost[0], cost[1])

        def dp(n):
            if mem[n] == -1:
                mem[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])
            return mem[n]

        return dp(n)




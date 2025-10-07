class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        size = len(coins)
        mem = [[-2] * (amount + 1) for _ in range(size)]

        def dfs(i, rest):
            # base cases
            if rest == 0:
                return 0

            if i == 0:
                if rest % coins[0] == 0:
                    return rest // coins[0]
                return float('inf')

            if mem[i][rest] != -2:
                return mem[i][rest]

            res = dfs(i - 1, rest)
            if rest >= coins[i]:
                res = min(res, dfs(i, rest - coins[i]) + 1)

            mem[i][rest] = res
            return res

        ans = dfs(size - 1, amount)
        return -1 if ans == float('inf') else ans

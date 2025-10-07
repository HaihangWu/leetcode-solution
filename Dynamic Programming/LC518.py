class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)
        mem = [[-1] * (amount + 1) for _ in range(size + 1)]

        def dfs(i, rest):
            if rest == 0:
                return 1
            if i == 0:
                return 0
            if mem[i][rest] != -1:
                return mem[i][rest]

            res = dfs(i - 1, rest)
            if rest >= coins[i - 1]:
                res += dfs(i, rest - coins[i - 1])

            mem[i][rest] = res
            return res

        return dfs(size, amount)

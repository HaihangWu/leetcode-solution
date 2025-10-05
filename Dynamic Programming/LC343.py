class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [-1] * (n + 1)
        mem[1] = 1

        def dfs(k):
            if mem[k] == -1:
                best = 0
                j = 1
                while j < k:
                    best = max(best, j * (k - j), dfs(j) * (k - j))
                    j += 1

                mem[k] = best

            return mem[k]

        return dfs(n)
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """


        size = len(strs)
        mem = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(size)]

        def dfs(i, t1, t2):
            if t1 < 0 or t2<0:
                return -float('inf')
            if i == 0:
                if t1>=strs[i].count('0') and t2>= strs[i].count('1'):
                    return 1
                return 0

            if mem[i][t1][t2] == -1:
                if strs[i].count('0') > m or strs[i].count('1') > n :
                    return dfs(i - 1, t1, t2)
                else:
                    mem[i][t1][t2] = max(dfs(i - 1, t1, t2), dfs(i - 1, t1-strs[i].count('0'), t2-strs[i].count('1'))+1)
            return mem[i][t1][t2]

        return dfs(size - 1, m, n)
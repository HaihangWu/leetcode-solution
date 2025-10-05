class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [-1] * (n + 2)
        mem[0]= 1
        mem[1] = 1
        mem[2] = 2

        def dfs(k):
            if mem[k] == -1:
                  j=0
                  mem[k]=0
                  while j < k:
                        mem[k] +=  dfs(k-1-j) *dfs(j)
                        j+=1
            return mem[k]

        return dfs(n)
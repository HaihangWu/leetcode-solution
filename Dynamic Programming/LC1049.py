class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        size=len(stones)
        target=sum(stones)//2
        mem=[ [-1]*(target+1) for _ in range(size)]


        def dfs(i, j):
            if j==0:
                mem[i][j]=0
            if i<0:
                mem[i][j]=0
            if  mem[i][j]==-1:
                if stones[i]>j:
                    return dfs(i-1,j)

                if stones[i]<=j:
                       mem[i][j]=max(
                        dfs(i-1,j),
                        dfs(i-1,j-stones[i])+stones[i])


            return mem[i][j]
        tmp=dfs(size-1,target)
        return abs(sum(stones)-2*tmp)


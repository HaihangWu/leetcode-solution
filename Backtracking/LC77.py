class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path=[]
        subpath=[]

        def backtracking(startindex):

            if len(subpath)==k:
                path.append(subpath[:])
                return

            for i in range(startindex, n+1):
                subpath.append(i)
                backtracking(i+1)
                subpath.pop()

        backtracking(1)

        return path

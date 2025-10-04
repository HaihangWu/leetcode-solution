class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        ans = []

        def backtracking():
            if len(ans) == n:
                res.append(ans[:])
                return
            for i in range(n):
                position = True
                if i in ans:  # same column check
                    position = False
                for index, ele in enumerate(ans):
                    if abs(i - ele) == len(ans) - index:  # diagonal check
                        position = False
                if position:
                    ans.append(i)
                    backtracking()
                    ans.pop()

        backtracking()
        return [["." * c + "Q" + "." * (n - c - 1) for c in solution] for solution in res]

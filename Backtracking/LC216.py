class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        answer = []

        def backtracking(start):
            if len(answer) == k:
                if sum(answer) == n:
                    res.append(answer[:])
                return

            for i in range(start, 10):
                answer.append(i)
                backtracking(i + 1)
                answer.pop()

        backtracking(1)
        return res


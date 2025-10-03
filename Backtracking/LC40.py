class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        answer = []
        size = len(candidates)
        candidates.sort()

        def backtracking(start, current_sum):

            if current_sum == target:
                res.append(answer[:])
                return

            if current_sum > target:
                return

            for index in range(start, size):
                if index > start and candidates[index] == candidates[index - 1]:
                    continue
                answer.append(candidates[index])
                backtracking(index + 1, current_sum + candidates[index])
                answer.pop()

        backtracking(0, 0)

        return res
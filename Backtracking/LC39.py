class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        answer = []
        size = len(candidates)

        def backtracking(start, candidates):

            if sum(answer) == target:
                res.append(answer[:])

                return

            if sum(answer) > target:
                return

            for index in range(start, size):
                answer.append(candidates[index])
                backtracking(index, candidates)
                answer.pop()
                # if len(answer)==0 and index<(size-1):
                #     candidates=candidates[index+1:]

        backtracking(0, candidates)

        return res


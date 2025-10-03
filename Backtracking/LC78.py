class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ans = []

        def backtracking(start):
            res.append(ans[:])  # add current subset
            for i in range(start, len(nums)):
                ans.append(nums[i])
                backtracking(i + 1)
                ans.pop()

        backtracking(0)
        return res
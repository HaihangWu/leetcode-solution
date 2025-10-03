class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        ans = []

        def backtracking(start):
            if ans not in res:
                res.append(ans[:])  # add current subset
            for i in range(start, len(nums)):
                ans.append(nums[i])
                backtracking(i + 1)
                ans.pop()

        backtracking(0)
        return res
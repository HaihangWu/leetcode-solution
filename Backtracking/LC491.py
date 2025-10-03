class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ans = []

        def backtracking(start):
            if ans not in res and len(ans)>=2:
                res.append(ans[:])  # add current subset
            for i in range(start, len(nums)):
                if len(ans)==0 or (len(ans)>0 and nums[i]>=ans[-1]):
                    ans.append(nums[i])
                    backtracking(i + 1)
                    ans.pop()

        backtracking(0)
        return res
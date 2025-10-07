class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        mem = [-1] * (size)

        def dfs(s):
            if s < 0:
                return 0
            if s == 0:
                return nums[0]
            if mem[s] == -1:
                mem[s] = max(dfs(s - 1), dfs(s - 2) + nums[s])
            return mem[s]

        return dfs(size - 1)

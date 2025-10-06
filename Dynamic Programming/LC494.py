class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        if target < -total or target > total:
            return 0
        dif = total - target
        if dif % 2 != 0:
            return 0
        goal = dif // 2
        n = len(nums)
        mem = [[-1] * (goal + 1) for _ in range(n)]

        def dfs(i, t):
            if t < 0:
                return 0
            if i == 0:
                if t == 0 and nums[0] == 0:
                    return 2
                if t == 0 or t == nums[0]:
                    return 1
                return 0

            if mem[i][t] == -1:
                if nums[i] > goal:
                    return dfs(i - 1, t)
                else:
                    mem[i][t] = dfs(i - 1, t) + dfs(i - 1, t - nums[i])
            return mem[i][t]

        return dfs(n - 1, goal)



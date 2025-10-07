class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 1:
            return nums[0]

        def rob_linear(arr):
            n = len(arr)
            mem = [-1] * n

            def dfs(i):
                if i < 0:
                    return 0
                if i == 0:
                    return arr[0]
                if mem[i] == -1:
                    mem[i] = max(dfs(i - 1), dfs(i - 2) + arr[i])
                return mem[i]

            return dfs(n - 1)

        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])

        return max(case1, case2)


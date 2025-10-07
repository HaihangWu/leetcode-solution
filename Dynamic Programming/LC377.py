class Solution(object):
    def combinationSum4(self, nums, target):
        mem = [-1] * (target + 1)
        mem[0] = 1  # base case：凑成0只有一种方式——不选任何数

        def dfs(rest):
            if mem[rest] != -1:
                return mem[rest]
            total = 0
            for num in nums:
                if num <= rest:
                    total += dfs(rest - num)
            mem[rest] = total
            return total

        return dfs(target)

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)

        # mem[i][j] 表示前 i 个数中，容量 j 的最大装载和
        mem = [[-1] * (target + 1) for _ in range(n)]

        def dfs(i, j):
            # base cases
            if j == 0:
                return 0
            if i < 0:
                return 0
            if mem[i][j] != -1:
                return mem[i][j]

            if nums[i] > j:
                res = dfs(i - 1, j)
            else:
                res = max(
                    dfs(i - 1, j),                  # 不取 nums[i]
                    dfs(i - 1, j - nums[i]) + nums[i]  # 取 nums[i]
                )
            mem[i][j] = res
            return res

        return dfs(n - 1, target) == target

# class Solution(object):
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         total = sum(nums)
#         if total % 2 != 0:
#             return False
#         target = total // 2
#
#         # 初始化一维数组，mem[j] 表示容量 j 下的最大装载和
#         mem = [0] * (target + 1)
#
#         # 递归 + 记忆化（扩容视角）
#         def dfs(j):
#             # 已经计算过的直接返回
#             if mem[j] != 0:
#                 return mem[j]
#
#             best = 0
#             for num in nums:
#                 if num <= j:
#                     best = max(best, dfs(j - num) + num)
#             mem[j] = best
#             return mem[j]
#
#         dfs(target)
#         return mem[target] == target


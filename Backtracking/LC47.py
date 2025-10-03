class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        size = len(nums)
        nums.sort()  # sort to handle duplicates
        used = [False] * size

        def backtracking():
            if len(ans) == size:
                res.append(ans[:])
                return
            for i in range(size):
                # skip already used
                if used[i]:
                    continue
                # skip duplicates: only allow the first unused occurrence
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                ans.append(nums[i])
                backtracking()
                ans.pop()
                used[i] = False

        backtracking()
        return res

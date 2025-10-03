class Solution(object):
    def permute(self, nums):
        res = []
        ans = []
        size = len(nums)
        used = [False] * size  # track whether nums[i] is used

        def backtracking():
            if len(ans) == size:
                res.append(ans[:])
                return
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    ans.append(nums[i])
                    backtracking()
                    ans.pop()
                    used[i] = False

        backtracking()
        return res
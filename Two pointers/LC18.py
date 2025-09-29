class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > (i + 1) and nums[j] == nums[j - 1]:
                    continue
                goal = target - (nums[i] + nums[j])
                left = j + 1
                right = n - 1
                while left < right:
                    if (nums[left] + nums[right]) == goal:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                        while nums[right] == nums[right + 1] and left < right:
                            right -= 1
                    elif nums[left] + nums[right] < goal:
                        left += 1
                    else:
                        right -= 1
        return res

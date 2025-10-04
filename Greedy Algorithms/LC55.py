class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_length = 0
        size = len(nums)
        for index, ele in enumerate(nums):
            if index <= max_length:
                i = index
                i += nums[i]
                if i >= (size - 1):
                    return True
                max_length = max(max_length, i)
        return False



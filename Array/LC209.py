class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = 0
        length = len(nums)
        result = length + 1
        sum = 0
        while right_index < length:
            sum += nums[right_index]
            while sum >= target:
                result = right_index - left_index + 1 if (right_index - left_index + 1) <= result else result
                sum -= nums[left_index]
                left_index = left_index + 1
            right_index += 1

        if result == length + 1:
            return 0
        else:
            return result
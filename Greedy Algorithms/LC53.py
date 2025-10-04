class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = nums[0]
        current_sum = 0
        consequtive = []
        for index, ele in enumerate(nums):
            consequtive.append(ele)
            current_sum = ele if len(consequtive) == 1 else current_sum + ele

            if current_sum < 0:
                consequtive = []
            largest_sum = max(current_sum, largest_sum)

        return largest_sum

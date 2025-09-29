class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        digits_info = {}
        for index, ele in enumerate(nums):
            tmp = target - ele
            if tmp not in digits_info.keys():
                digits_info[ele] = index
            else:
                return [index, digits_info[tmp]]
        return False

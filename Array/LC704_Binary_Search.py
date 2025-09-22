class Solution(object):
    def search(self, nums, target):

        searching_starting_index = 0
        searching_end_index = len(nums) - 1
        if target > nums[searching_end_index] or target < nums[searching_starting_index]:
            return -1

        while searching_starting_index <= searching_end_index:

            searching_middle_index = (searching_starting_index + searching_end_index) // 2

            if target == nums[searching_end_index]:
                return searching_end_index
            elif target == nums[searching_starting_index]:
                return searching_starting_index
            elif target == nums[searching_middle_index]:
                return searching_middle_index
            elif (searching_end_index - searching_starting_index) == 1:
                return -1

            if target > nums[searching_middle_index]:
                searching_starting_index = searching_middle_index
            elif target < nums[searching_middle_index]:
                searching_end_index = searching_middle_index
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        mid = (n + 1) // 2
        small, large = nums[:mid][::-1], nums[mid:][::-1]

        nums[::2] = small
        nums[1::2] = large
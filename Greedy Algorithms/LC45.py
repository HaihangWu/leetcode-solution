class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 1:
            return 0

        jump = 0
        max_length = 0
        res_pre = {0}

        while res_pre:
            jump += 1
            res_post = set()

            for index in res_pre:
                furthest = index + nums[index]
                if furthest >= size - 1:
                    return jump
                res_post.update(range(index + 1, furthest + 1))

            res_pre = res_post

        return jump

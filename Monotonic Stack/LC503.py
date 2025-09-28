class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = deque()
        n = len(nums)
        answer = [-1] * n
        for iter in range(2):
            for index, ele in enumerate(nums):
                while stack:
                    if nums[stack[-1]] < ele:
                        answer[stack[-1]] = ele
                        stack.pop()
                    else:
                        break
                if iter == 0:
                    stack.append(index)
        return answer


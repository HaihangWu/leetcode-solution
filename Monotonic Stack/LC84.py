class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = deque()
        answer = [0] * len(heights)
        heights = [0] + heights + [0]
        max_area = 0
        for index, height in enumerate(heights):
            while stack:
                if height >= heights[stack[-1]]:
                    break
                else:
                    tmp = stack.pop()
                    answer[tmp - 1] = heights[tmp] * (index - stack[-1] - 1)
                    max_area = max(max_area, heights[tmp] * (index - stack[-1] - 1))
            stack.append(index)
        return max_area


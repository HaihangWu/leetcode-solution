class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        stack = deque()
        rain_amount = 0
        for index, ele in enumerate(height):
            while stack:
                if ele > height[stack[-1]]:
                    bottom = stack.pop()
                    lowest = height[bottom]
                else:
                    break
                if len(stack) == 0:
                    break
                else:
                    rain_amount += (min(ele, height[stack[-1]]) - lowest) * (index - stack[-1] - 1)
            stack.append(index)
        return rain_amount

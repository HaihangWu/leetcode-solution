class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [None] * n
        stack = deque()
        for i in range(n):
            while stack:
                if temperatures[stack[-1]] < temperatures[i]:
                    if answer[stack[-1]] is None:
                        answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(i)
        return [ele if ele is not None else 0 for ele in answer]


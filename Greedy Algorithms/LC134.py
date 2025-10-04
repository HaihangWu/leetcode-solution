class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        stations = len(gas)
        if sum(gas) < sum(cost):
            return -1

        residual = [gas[i] - cost[i] for i in range(stations)]
        start = 0
        curSum = 0

        for i in range(stations):
            curSum += residual[i]
            if curSum < 0:
                start = i + 1  # 重新从下一个站点尝试
                curSum = 0

        return start if start < stations else -1

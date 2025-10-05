class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 按起点排序
        intervals.sort(key=lambda x: x[0])

        res = []
        cur_start, cur_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= cur_end:
                cur_end = max(cur_end, end)
            else:
                res.append([cur_start, cur_end])
                cur_start, cur_end = start, end

        res.append([cur_start, cur_end])
        return res

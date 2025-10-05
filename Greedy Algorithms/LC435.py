class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        arrows = 1
        removed = 0
        cur_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < cur_end:
                removed += 1
            else:
                cur_end = end

        return removed

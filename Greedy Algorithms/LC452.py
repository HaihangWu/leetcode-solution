class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        cur_end = points[0][1]
        print(points)

        for start, end in points[1:]:
            if start > cur_end:
                arrows += 1
                cur_end = end

        return arrows

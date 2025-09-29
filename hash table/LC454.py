class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sum_12 = {}
        count = 0
        for ele1 in nums1:
            for ele2 in nums2:
                sum_tmp = ele1 + ele2
                if sum_tmp in sum_12:
                    sum_12[sum_tmp] += 1
                else:
                    sum_12[sum_tmp] = 1

        for ele3 in nums3:
            for ele4 in nums4:
                sum_tmp = ele3 + ele4
                if -sum_tmp in sum_12:
                    count += sum_12[-sum_tmp]
        return count
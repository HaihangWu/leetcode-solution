class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1_set=set(nums1)
        s2_set=set(nums2)
        result=[]
        for ele in s2_set:
            if ele in s1_set:
                result.append(ele)
        return result
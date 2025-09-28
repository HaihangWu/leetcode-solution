class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s12 = {}
        result = [-1] * len(nums1)
        stack = deque()
        for index, ele in enumerate(nums1):
            s12[ele] = index
        for index, ele in enumerate(nums2):
            while stack:
                if stack[-1] < ele:
                    if stack[-1] in s12.keys():
                        result[s12[stack[-1]]] = ele
                    stack.pop()
                else:
                    break
            stack.append(ele)
        return result

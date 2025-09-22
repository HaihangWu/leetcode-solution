class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        left=0
        right=len(nums)-1

        while left<=right:
            left_square=nums[left]*nums[left]
            right_square=nums[right]*nums[right]
            if left_square<right_square:
                result.append(right_square)
                right-=1
            else:
                result.append(left_square)
                left+=1

        result.reverse()
        return result
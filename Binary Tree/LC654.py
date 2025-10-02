# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(nums) == 0:
            return None
        root_val = max(nums)
        index = nums.index(root_val)
        root = TreeNode(root_val)
        left_tree = nums[0:index]
        right_tree = nums[index + 1:]
        root.left = self.constructMaximumBinaryTree(left_tree)
        root.right = self.constructMaximumBinaryTree(right_tree)

        return root


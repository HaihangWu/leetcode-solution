# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        if root.val == val:
            return root
        root_left = self.searchBST(root.left, val)
        if root_left is None:
            root_right = self.searchBST(root.right, val)
            if root_right is None:
                return None
            else:
                return root_right
        else:
            return root_left


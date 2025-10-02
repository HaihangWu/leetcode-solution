# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree_max(self, root):
        if root is None:
            return None
        max_tmp = root.val
        if root.left is not None:
            left_max = self.tree_max(root.left)
            max_tmp = max(max_tmp, left_max)
        if root.right is not None:
            right_max = self.tree_max(root.right)
            max_tmp = max(max_tmp, right_max)
        return max_tmp

    def tree_min(self, root):
        if root is None:
            return None
        min_tmp = root.val
        if root.left is not None:
            left_min = self.tree_min(root.left)
            min_tmp = min(min_tmp, left_min)
        if root.right is not None:
            right_min = self.tree_min(root.right)
            min_tmp = min(min_tmp, right_min)
        return min_tmp

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is not None:
            left_max = self.tree_max(root.left)
            print(left_max)
            if root.val <= left_max or not self.isValidBST(root.left):
                return False

        if root.right is not None:
            right_min = self.tree_min(root.right)
            print(right_min)
            if root.val >= right_min or not self.isValidBST(root.right):
                return False

        return True

        left_tree_max = self.tree_max(root.left)
        right_tree_min = self.tree_max(root.right)


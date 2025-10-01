# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def order(self, root):
        if root is None:
            return

        root.left, root.right = root.right, root.left

        self.order(root.left)
        self.order(root.right)

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.order(root)
        return root

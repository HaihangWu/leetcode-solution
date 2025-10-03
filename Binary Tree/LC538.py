# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root
        if root.right is not None:
            root.right = self.convertBST(root.right)
            tmp = root.right
            while tmp.left is not None:
                tmp = tmp.left
            root.val += tmp.val
        if root.left is not None:
            tmp = root.left
            while tmp.right is not None:
                tmp = tmp.right
            tmp.val += root.val
            root.left = self.convertBST(root.left)

        return root

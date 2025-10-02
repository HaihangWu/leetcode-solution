# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root1 is None and root2 is None:
            return None
        root = TreeNode()
        if root1 is None:
            root.val = root2.val
            root.left = self.mergeTrees(None, root2.left)
            root.right = self.mergeTrees(None, root2.right)
        elif root2 is None:
            root.val = root1.val
            root.left = self.mergeTrees(root1.left, None)
            root.right = self.mergeTrees(root1.right, None)
        else:
            root.val = root1.val + root2.val
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        return root

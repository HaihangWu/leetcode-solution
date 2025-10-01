# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if not t1 or not t2:
            return False

        return (t1.val==t2.val and self.mirror(t1.left, t2.right) and self.mirror(t1.right, t2.left))

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        return self.mirror(root.left,root.right)
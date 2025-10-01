# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def order(self, root, res):
        if root is None:
            return

        res.append(root.val)
        self.order(root.left, res)
        self.order(root.right, res)

    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = []
        self.order(root, res)
        return len(res)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def Traverse(self, root, res):
        if root is None:
            return
        self.Traverse(root.left, res)
        self.Traverse(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.Traverse(root, res)
        return res

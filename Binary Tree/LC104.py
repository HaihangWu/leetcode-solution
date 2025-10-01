# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def order(self, root, depth, res):
        if root is None:
            return

        if (len(res) == depth):
            res.append([])

        res[depth].append(root.val)
        self.order(root.left, depth + 1, res)
        self.order(root.right, depth + 1, res)

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        depth = 0
        self.order(root, depth, res)
        return len(res)

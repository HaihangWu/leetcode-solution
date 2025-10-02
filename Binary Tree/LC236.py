# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left_ancestor = None
        right_ancestor = None

        if root.left is not None:
            left_ancestor = self.lowestCommonAncestor(root.left, p, q)

        if root.right is not None:
            right_ancestor = self.lowestCommonAncestor(root.right, p, q)

        if left_ancestor is None and right_ancestor is None:
            return None

        if left_ancestor is not None and right_ancestor is not None:
            return root

        if left_ancestor is not None:
            return left_ancestor

        if right_ancestor is not None:
            return right_ancestor

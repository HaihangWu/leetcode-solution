# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def left_sum(node):
            total=0
            if node.left:
                if node.left.left is None and node.left.right is None:
                    total+=node.left.val
                else:
                    total+=left_sum(node.left)
            if node.right:
                if node.right.left is None and node.right.right is None:
                    total+=0
                else:
                    total+=left_sum(node.right)
            return total
        return left_sum(root)
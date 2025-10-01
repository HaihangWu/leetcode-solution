# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def path_sum(node):
            all_sum = []
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            for child in (node.left, node.right):
                for ele in path_sum(child):
                    all_sum.append(node.val + ele)

            return all_sum

        return targetSum in path_sum(root)

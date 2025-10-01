# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        def path_sum(node):
                sub_paths = []
                if node is None:
                    return []
                if node.left is None and node.right is None:
                    return [[node.val]]
                for child in (node.left, node.right):
                    for ele in path_sum(child):
                        sub_paths.append([node.val] + ele)

                return sub_paths

        res=[]
        for path in path_sum(root):
            if sum(path)==targetSum:
                res.append(path)
        return res
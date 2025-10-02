# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder) == 0:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        d_index = inorder.index(root_val)

        left_tree_in = inorder[0:d_index]
        right_tree_in = inorder[d_index + 1:]

        left_tree_pre = preorder[1:d_index + 1]
        right_tree_pre = preorder[d_index + 1:]

        root.left = self.buildTree(left_tree_pre, left_tree_in)
        root.right = self.buildTree(right_tree_pre, right_tree_in)

        return root
